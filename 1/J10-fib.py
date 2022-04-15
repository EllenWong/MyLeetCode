'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）
'''

#---------------一般求解方式----------------------
class Solution:
    def fib(self, n: int) -> int:
        f = [0,1]
        for i in range(2,n+1):
            f.append((f[i-1]+f[i-2])%1000000007)
        return f[n]

# ----------------滚动数组------------------------
class Solution2:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n
        p, q, r = 0, 0, 1 #只需定义三个变量，空间复杂度为O(n)
        for i in range(2, n + 1):
            p = q
            q = r
            r = (p + q) % MOD
        return r

# ------------------快速幂-------------------------
class Solution3:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]: #定义矩阵乘法
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c

        def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]: #快速幂进行问题求解
            ret = [[1, 0], [0, 1]] #定义一个单位阵
            while n > 0:
                if n & 1: #指数为奇数时
                    ret = multiply(ret, a) #ret_n = ret_n-1 * a
                n >>= 1 # n = n /2
                a = multiply(a, a) # ret_n = ret_n/2 * ret_n/2
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n - 1) #时间复杂度O(logn)空间复杂度O(n)
        return res[0][0]


s=Solution()
print(s.fib(5))