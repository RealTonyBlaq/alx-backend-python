#!/usr/bin/env python3
"""
task_wait_random that takes an integer max_delay
and returns a asyncio.Task
"""

import asyncio
from typing import TypeVar


wait_random = __import__('0-basic_async_syntax').wait_random
asyncio


def task_wait_random(max_delay: int):
    """ Returns an asyncio.Task """
    return asyncio.Task(wait_random(max_delay))
