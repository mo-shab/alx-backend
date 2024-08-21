#!/usr/bin/python3
"""[LFU caching]"""

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.key_freq = {}
        self.freq_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._increase_freq(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self._evict()

            self.cache_data[key] = item
            self.key_freq[key] = 1
            self.freq_keys[1][key] = None
            self.min_freq = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self._increase_freq(key)
        return self.cache_data[key]

    def _increase_freq(self, key):
        """ Helper function to increase the frequency of a key """
        freq = self.key_freq[key]
        del self.freq_keys[freq][key]

        if not self.freq_keys[freq]:
            del self.freq_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        self.key_freq[key] += 1
        new_freq = self.key_freq[key]
        self.freq_keys[new_freq][key] = None

    def _evict(self):
        """ Evict the least frequently used key """
        lfu_key, _ = self.freq_keys[self.min_freq].popitem(last=False)

        if not self.freq_keys[self.min_freq]:
            del self.freq_keys[self.min_freq]

        del self.cache_data[lfu_key]
        del self.key_freq[lfu_key]
        print(f"DISCARD: {lfu_key}")
