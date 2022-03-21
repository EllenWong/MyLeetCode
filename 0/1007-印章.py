'''
问题描述
　　共有n种图案的印章，每种图案的出现概率相同。小A买了m张印章，求小A集齐n种印章的概率。
输入格式
　　一行两个正整数n和m
输出格式
　　一个实数P表示答案，保留4位小数。
样例输入
2 3
样例输出
0.7500
数据规模和约定
　　1≤n，m≤20
'''

# ---------------Wrong------------------
# import math

# n,m = map(int,input().split())
# # print(n,m)
# # print(1.0/math.pow(n,n))
# res = math.comb(m,n)*1.0/math.pow(n,n)
# print("%.4f"% res)

#——————————————————————DP——————————————————————

import math
n,m = map(int,input().split()) # 一共有n种印章，收集了m种印章，求收集齐n种印章的概率

# 用dp[m][n]表示最终的结果，dp[i][j] 表示当前状态收集了i个印章，一共有j种印章，此时收集完j种印章的概率

dp = [[0 for i in range(21)] for j in range(21)]
dp1 = [[0]*25]*25 #一般不用于动态规划的赋值，
# print(dp1)
# print(dp)

for i in range(1,m+1):
    for j in range(1,n+1):
        if j > i:
            dp[i][j] = 0
            # print(i,' ',j,dp[i][j])
        elif j == 1:
            dp[i][j] = 1/n**(i-1)
            # print(i,' ',j,dp[i][j])
        else:
            dp[i][j] = dp[i-1][j]*j/n + dp[i-1][j-1]*(n-j+1)/n
            # print(i,' ',j,dp[i][j])

# for i in range(1,m+1):
#     for j in range(1,n+1):
#         print(dp[i][j],' ',end='')
#     print('\n',end='')
# print(dp)
print("%.4f" %dp[m][n])

