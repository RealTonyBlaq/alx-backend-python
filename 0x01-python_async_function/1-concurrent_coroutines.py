#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments:
n and max_delay. You will spawn wait_random n times with
the specified max_delay.
"""

import asyncio


wait_random = __import__('./0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) :
