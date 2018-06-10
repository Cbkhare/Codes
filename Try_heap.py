import heapq as H # from heapq import *

x = [[1,3,4,2],[5,2,5,6],[9,1,2,3]]
x = str(x).replace('[','').replace(']','').split(', ')
x = list(map(int, x ))

y = []

for v in x:
    H.heappush(y, v)

for i in range(len(y)):
    print (H.heappop(y))
