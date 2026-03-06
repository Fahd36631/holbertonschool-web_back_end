#!/usr/bin/env python3
"""Simple helper function to calculate pagination index range."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end indexes."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
    