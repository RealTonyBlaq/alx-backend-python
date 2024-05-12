#!/usr/bin/env python3
"""
async_generator - takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int]:
    """ Coroutine loops 10 times, yields a random number each time """
    async for i in range(10):
        yield i
