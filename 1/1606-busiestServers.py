from typing import List
from sortedcontainers import SortedList
import heapq as hq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k)) #存储空闲服务器编号
        busy = [] #优先队列，队首服务器最早处理完请求
        requests = [0] * k #对应的服务器可处理的请求的数目
        # >>> a = [1,2,3]
        # >>> b = [4,5,6]
        # >>> zipped = zip(a,b)     # 打包为元组的列表
        # >>> [(1, 4), (2, 5), (3, 6)]
        for i, (start, t) in enumerate(zip(arrival, load)): #enumerate用于可遍历的数据对象，zip将一个个元素打包成一个元组
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                hq.heappop(busy)

            if len(available) == 0: #当前没有可用的服务器
                continue

            j = available.bisect_left(i % k) #j去访问下一个可以利用的服务器
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1 # 序号为id的服务器处理的请求增加1

            hq.heappush(busy, (start + t, id)) #对busy的处理，二维数组
            available.remove(id)

        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]

k = 3
arrival = [1,2,3,4,5]
load = [5,2,3,3,3]
s = Solution()
print(s.busiestServers(k,arrival,load))