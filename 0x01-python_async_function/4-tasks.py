#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random
is being called.
"""

import asyncio


task_wait_random = __import__('3-tasks').task

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns wait_random n times and saves the delay to a list """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    tasks = await asyncio.gather(*delays)
    return sorted(tasks)
