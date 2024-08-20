#!/usr/bin/python3
"""[LIFO caching]"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ LIFOCache class
        - inherits from BaseCaching and implements a LIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
            If the cache exceeds MAX_ITEMS, remove the newest item.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in\
                self.cache_data:
            newest_key = next(reversed(self.cache_data))
            print(f"DISCARD: {newest_key}")
            self.cache_data.pop(newest_key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
            If key is None or if the key doesn’t exist in self.cache_data,
            return None.
        """
        return self.cache_data.get(key)
