from sys import stdin as si
from functools import cmp_to_key

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def merge(self, one, two):
        s = min(one.start, two.start)
        e = max(one.end, two.end)
        merge = Interval(s,e)
        return merge

    #def insert(self, int_list, new):
        #result = [new]

    def insert(self, int_list):
        result = [int_list[0]]
        for i in int_list[1:]:
            last = result.pop()
            if last.start <= i.start <= last.end or last.start <= i.end <= \
                    last.end:
                # merge is needed
                result.append(self.merge(last,i))
            elif i.end < last.start :
                # change order
                result.append(i)
                result.append(last)
            elif last.end < i.start:
                # change order
                result.append(last)
                result.append(i)
        return result

i1=Interval(0,3)
i2=Interval(1,2)
i3=Interval(5,8)
i4=Interval(6,9)
st=Solution()
for val in st.insert([i1,i2,i3,i4]):
    print (val.start,val.end)