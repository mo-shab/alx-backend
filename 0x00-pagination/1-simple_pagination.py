#!/usr/bin/env python3
"""Simple helper function to paginate a dataset."""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset, loads it from the CSV
        file if not already loaded.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of rows from the dataset corresponding to
        the specified page and page size.
        """
        assert isinstance(page, int) and page > 0, "Page must be an integer\
              greater than 0."
        assert isinstance(page_size, int) and page_size > 0, "Page size must\
            be an integer greater than 0."

        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of start and end index for the given
    pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
