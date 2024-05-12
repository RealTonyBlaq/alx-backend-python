#!/usr/bin/env python3
"""
measure_runtime - coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures the total runtime and returns it """
    
