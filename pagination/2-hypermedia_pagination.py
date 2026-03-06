#!/usr/bin/env python3
"""Hypermedia pagination implementation with HATEOAS support.
"""
import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Retrieve and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of the dataset.

        Args:
            page (int, optional): The page number (1-indexed). Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows for the requested page, or empty list if out of range.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
            Dict[str, Union[List[List], None, int]]:
        """Retrieve a page with hypermedia pagination metadata.

        Args:
            page (int, optional): The page number (1-indexed). Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Union[List[List], None, int]]: A dictionary containing page data
            and hypermedia pagination metadata (HATEOAS).
        """
        data: List = self.get_page(page, page_size)
        size_dataset: int = len(self.dataset())
        total_pages = math.ceil(size_dataset / page_size)
        prev_page = None if page - 1 == 0 else page - 1
        next_page = None if page >= total_pages else page + 1
        actual_page_size = len(data)
        hateoas: Dict = {'page_size': actual_page_size,
                         'page': page,
                         'data': data,
                         'next_page': next_page,
                         'prev_page': prev_page,
                         'total_pages': total_pages}
        return hateoas
        