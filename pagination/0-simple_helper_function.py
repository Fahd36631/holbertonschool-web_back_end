#!/usr/bin/env python3
"""Simple helper function to calculate pagination index range.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return (start, end)
    