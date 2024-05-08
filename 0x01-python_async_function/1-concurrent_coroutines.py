#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments:
n and max_delay. You will spawn wait_random n times with
the specified max_delay
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns wait_random n times and saves the delay to a list """
    delays = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)
