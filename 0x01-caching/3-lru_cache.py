#!/usr/bin/python3
"""[LRU caching]"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class
        - inherits from BaseCaching and implements a LRU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
            If the cache exceeds MAX_ITEMS, remove the Least recently used
            item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Remove the first item (least recently used) if the cache is full
            oldest_key = next(iter(self.cache_data))
            print(f"DISCARD: {oldest_key}")
            self.cache_data.pop(oldest_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
            If the key exists, move it to the end to mark it as recently used.
        """
        if key not in self.cache_data:
            return None
        # Move the accessed key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
