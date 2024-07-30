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

import linecache
import tracemalloc
from dlrover.python.common.log import default_logger as logger


K = 1024


def display_top_memory_using(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    logger.info(f"Top {limit} memory-using:")
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        logger.info(f"#{index}: {frame.filename}:{frame.lineno}: {stat.size / K:.1f} KiB")
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            logger.info(f"------> {line}")

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        logger.info(f"{len(other)} other: {size / K:.1f} KiB")
    total = sum(stat.size for stat in top_stats)

    logger.info(f"Total allocated size: {(total / K):.1f} KiB")
