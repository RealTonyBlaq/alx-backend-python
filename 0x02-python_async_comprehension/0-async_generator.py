#!/usr/bin/env python3
"""
async_generator - takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """ Coroutine loops 10 times, yields a random number each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
