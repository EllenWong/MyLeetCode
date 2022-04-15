from secrets import choice

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.dict = {} #数组不能在单位时间内进行元素判断与删除

    def insert(self, val: int) -> bool:
        if val in self.dict: return False # val 已存在，返回False
        self.dict[val] = len(self.nums) #字典表示val的值对应的id
        self.nums.append(val) #添加当前元素
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict: return False #val不存在，返回False
        id = self.dict[val] #访问val对应的id
        self.nums[id] = self.nums[-1] #用最后一个数进行填充
        self.dict[self.nums[id]] = id #更改对应的id
        self.nums.pop() #列表删除
        del self.dict[val] #字典删除
        return True

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()