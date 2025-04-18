# Copyright 2024 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import asyncio
import os
import signal
import threading
import time

import psutil
import tornado
from tornado.ioloop import IOLoop
from tornado.netutil import bind_sockets

from dlrover.python.common.log import default_logger as logger
from dlrover.python.util.common_util import is_port_in_use


def is_asyncio_loop_running():
    try:
        asyncio.get_running_loop()
        return True
    except RuntimeError:
        return False


class CustomHTTPServer(abc.ABC):
    """Self designed http server."""

    def __init__(self, address, port, handler_classes):
        self._address = address
        self._port = port
        self._handler_classes = handler_classes

    @property
    def address(self):
        return self._address

    @property
    def port(self):
        return self._port

    @property
    def handler_classes(self):
        return self._handler_classes

    @abc.abstractmethod
    def start(self):
        """Start the server."""
        pass

    @abc.abstractmethod
    def stop(self, grace=None):
        """
        Stop the server.

        Arg:
            grace (Optional[float]): Grace period.
        """
        pass


class TornadoHTTPServer(CustomHTTPServer):

    SERVING_THREAD_NAME = "http-server-serving-thread"

    def __init__(self, address, port, handler_class):
        super().__init__(address, port, handler_class)

        self._server = None
        self._server_thread = None
        self._serving_started = False
        self._stop_event = threading.Event()

        signal.signal(signal.SIGINT, lambda sig, frame: self.stop())
        signal.signal(signal.SIGTERM, lambda sig, frame: self.stop())

    def start(self):
        if not self.is_serving():
            logger.info("Starting http server...")
            self._serving_started = True
            self._server_thread = threading.Thread(
                name=TornadoHTTPServer.SERVING_THREAD_NAME,
                target=self._start,
                daemon=True,
            )
            self._server_thread.start()

            while True:
                if is_port_in_use(self._port):
                    break
                time.sleep(0.5)

    @classmethod
    def _cal_process_num_by_cpu(cls):
        cpu_num = os.cpu_count()
        if cpu_num <= 2:
            return 1
        elif 2 < cpu_num <= 8:
            return cpu_num - 1
        elif 8 < cpu_num <= 16:
            return cpu_num - 2
        else:
            return cpu_num - 4

    def _start(self):
        try:
            sockets = bind_sockets(self._port)

            http_process_num = self._cal_process_num_by_cpu()
            logger.info(
                f"Use {http_process_num} processes for "
                f"tornado http server."
            )
            tornado.process.fork_processes(http_process_num)

            self._server = tornado.httpserver.HTTPServer(
                tornado.web.Application(self._handler_classes)
            )
            self._server.add_sockets(sockets)
            logger.info(
                f"Http server process {os.getpid()} running "
                f"on port {self._port}"
            )

            while not self._stop_event.is_set():
                IOLoop.current().start()
        except Exception as e:
            if not self._stop_event.is_set():
                logger.error(f"Http server start with error: {e}")
            IOLoop.current().stop()
        finally:
            logger.info(f"Cleanly shutting down process {os.getpid()}...")
            self._server.stop()
            IOLoop.current().stop()

    def stop(self, grace=None):
        if self._server_thread:
            self._stop_event.set()
            self._server_thread.join(timeout=5)

            for child in psutil.Process(os.getpid()).children(recursive=True):
                logger.info(f"Terminating child process: {child.pid}...")
                child.terminate()
                child.wait(timeout=5)

        self._serving_started = False

    def is_serving(self):
        return self._serving_started
