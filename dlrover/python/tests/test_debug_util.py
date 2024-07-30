# Copyright 2022 The DLRover Authors. All rights reserved.
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

import threading
import time
import tracemalloc
import unittest

import dlrover.python.util.debug_util as du


class DebugUtilTest(unittest.TestCase):
    def test_display_top_memory_using(self):
        tracemalloc.start()

        data1 = [x * 2 for x in range(100000)]
        self.assertIsNotNone(data1)
        data2 = [x * 3 for x in range(100000)]
        self.assertIsNotNone(data2)

        snapshot = tracemalloc.take_snapshot()
        du.display_top_memory_using(snapshot)

        result = []

        def async_test(return_list):
            i = 0
            while i < 5:
                return_list.append([i * 2 for x in range(100000)])
                i += 1
                time.sleep(1)

        threading.Thread(
            target=async_test,
            kwargs={"return_list": result},
            name="async_test",
            daemon=True
        ).start()

        for _ in range(10):
            snapshot = tracemalloc.take_snapshot()
            du.display_top_memory_using(snapshot, limit=3)
            time.sleep(0.5)
