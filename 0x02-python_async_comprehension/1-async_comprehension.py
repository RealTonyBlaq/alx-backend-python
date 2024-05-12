#!/usr/bin/env python3
"""
async_comprehension - takes no arguments.
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers
"""

import asyncio
from typing import List


generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers comprehensing over async_generator
    and returns a list of the numbers
    """
    numbers = [i async for i in generator()]
    return numbers
