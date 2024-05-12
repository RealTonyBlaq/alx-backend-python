#!/usr/bin/env python3
"""
async_generator - takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module
"""

import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """ Coroutine loops 10 times, yields a random number each time """
    for i in range(10):
        yield random.uniform(0.000, 10.000)
        await asyncio.sleep(1.00)
