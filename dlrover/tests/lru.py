"""LRU缓存"""
import collections


class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.deq = collections.deque()
        self.capacity = capacity
        self.size = 0

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.deq.remove(key)
            self.deq.append(key)
        else:
            if len(self.cache) > self.capacity:
                to_delete = self.deq.popleft()
                del self.cache[to_delete]
            self.cache[key] = value
            self.deq.append(key)
            self.size += 1

    def get(self, key):
        if key in self.cache:
            self.deq.remove(key)
            self.deq.append(key)
            return self.cache[key]
        else:
            return None

