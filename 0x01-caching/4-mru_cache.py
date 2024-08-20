#!/usr/bin/python3
"""[MRU caching]"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache class
        - inherits from BaseCaching and implements a MRU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
            If the cache exceeds MAX_ITEMS, remove the Most recently used
            item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Remove the last item (most recently used) if the cache is full
            last_key = next(reversed(self.cache_data))
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
            If the key exists, move it to the end to mark it as recently used.
        """
        if key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
