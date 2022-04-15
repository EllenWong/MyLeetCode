from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] #小顶堆，存储较大的一半数据 python中的堆默认用小顶堆存储
        self.B = [] #大顶堆，存储较小的一半数据 使用大顶堆，可以直接将堆中元素取反

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B): #当A，B中元素数量不相等时，插入元素应放入B中
            heappush(self.A,num) #先将元素放到A堆中
            heappush(self.B,-heappop(self.A)) #将A的顶部元素（较大的一部分数据中最小的一个）弹出，取反放入B中
        else: #当A，B中元素数量相等时，插入元素应放入A中
            heappush(self.B,-num) #先将元素放入B中，注意需要取反
            heappush(self.A,-heappop(self.B)) #将B中的顶部元素弹出，取反放入A中

    def findMedian(self) -> float:
        if len(self.A) != len(self.B): #总体元素数目为奇数时
            return self.A[0]
        else:
            return (self.A[0]-self.B[0])/2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()