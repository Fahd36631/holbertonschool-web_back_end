#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination implementation.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Create and cache an indexed version of the dataset.

        Returns:
            Dict[int, List]: A dictionary mapping index to dataset row.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve a page using index-based pagination that is resilient to deletions.

        Args:
            index (int, optional): The starting index for pagination. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing the page data and pagination metadata.
        """
        assert index is not None
        len_data = len(self.dataset())
        assert 0 <= index < len_data

        indexed_dataset = self.indexed_dataset()
        data = []
        current_index = index
        next_index = None
        
        while len(data) < page_size and current_index < len_data:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1
        
        if current_index < len_data:
            next_index = current_index
        
        indexed_data = {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
        return indexed_data
        