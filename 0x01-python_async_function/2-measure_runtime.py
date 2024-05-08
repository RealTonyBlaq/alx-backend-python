#!/usr/bin/env python3
"""
Creates a measure_time function with integers n and max_delay
as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n.
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures runtime and returns a float total_time / n """
    begin = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - begin
    return (end / n)
