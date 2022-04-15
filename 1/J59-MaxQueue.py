import collections

class MaxQueue:

    def __init__(self):
        self.q = collections.deque()

    def max_value(self) -> int:
        if self.q: return max(self.q)
        else: return -1

    def push_back(self, value: int) -> None:
        self.q.append(value)

    def pop_front(self) -> int:
        if self.q: return self.q.popleft()
        else: return -1



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()