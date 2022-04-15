'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

'''

from inspect import stack


#queue:先入先出
#stack：先入后出


class CQueue:

    def __init__(self):
        self.stack1 = []  #用列表的形式实现栈的操作（先入先出）
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value) #在列表的末尾增加一个新的值value

    def deleteHead(self) -> int:
        if self.stack2:  
            return self.stack2.pop()        
        if not self.stack1: #当原来的栈是空的时，直接返回-1
            return -1
        while self.stack1: #当stack1不为空的时候
            self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()

c = CQueue()
c.appendTail(3)
print(c.deleteHead())
print(c.deleteHead())



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()