#!/usr/bin/env python3
"""
Annotating the below functions parameters
and return values with the appropriate types
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a List of Tuples """
    return [(i, len(i)) for i in lst]
