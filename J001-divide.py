class Solution:
    def divide(self, a: int, b: int) -> int:
        # 对最大最小值的考虑
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if a == INT_MIN :
            if b == 1:
                return INT_MIN
            if b == -1:
                return INT_MAX
        if b == INT_MIN:
            return 1 if a == INT_MIN else 0
        if a == 0: return 0
        # 对符号位的考虑
        sign = -1 if (a>0) ^ (b>0) else 1
        a,b = -abs(a),-abs(b) # 以负数的情况考虑
        candidates = [b] # 候选集合
        while candidates[-1] >= a - candidates[-1]:
            candidates.append(candidates[-1] + candidates[-1])

        c = 0 #存储最终结果
        # 逆序遍历的情况
        for i in range(len(candidates)-1 , -1,-1):
            if candidates[i] >= a:
                c += (1<<i)
                a -= candidates[i]
        return c if sign==1 else -c