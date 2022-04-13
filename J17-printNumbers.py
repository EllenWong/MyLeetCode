# 剑指 Offer 17. 打印从1到最大的n位数
class Solution:
    def printNumbers(self, n: int):
        def dfs(x):
            if x == n: #遍历到第n位时
                s = ''.join(num[self.start:]) #s去掉前置0
                if s != '0': res.append(int(s)) # res存储时转换为int类型
                # 当出现进位时，前置0的个数-1
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10): #对当前位进行遍历0～9
                if i == 9: self.nine += 1 #记录9 是否出现
                num[x] = str(i) #更改当前数值的第x位为i
                dfs(x + 1) #递归判读下一位
            self.nine -= 1
        
        num, res = ['0'] * n, [] 
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res