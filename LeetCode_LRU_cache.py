from collections import OrderedDict as D
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = D()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.d.move_to_end(key)
        return self.d.get(key,-1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            self.d[key] = value
            self.d.move_to_end(key)
        else:
            if self.capacity==0:
                self.d.popitem(last=False)
            else:
                self.capacity-=1
            self.d.update({key: value})


'''
https://leetcode.com/problems/lru-cache/description/
'''