'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    def movingCount(self, m: int, n: int, k: int) -> int:
        '''用于计算某一个数字的数位和'''
        def kk(i): 
            res = 0
            while i:
                res = res + i%10
                i = i//10
            return res


        vis = set([(0,0)]) #定义一个集合，集合内元素不重复，表示该位置可到达，空间复杂度为O(mn)
        for i in range(m):
            for j in range(n):#对整个表进行遍历，时间复杂度为O(mn)
                if (((i-1,j) in vis) or ((i,j-1) in vis)) and kk(i)+kk(j)<=k:
                    vis.add((i,j)) #如果上一步的位置在集合中，以及满足约束条件，则添加当前位置到集合中

        return len(vis)