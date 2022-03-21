'''
问题描述
　　有一个N x N的方格,每一个格子都有一些金币,只要站在格子里就能拿到里面的金币。你站在最左上角的格子里,每次可以从一个格子走到它右边或下边的格子里。请问如何走才能拿到最多的金币。
输入格式
　　第一行输入一个正整数n。
　　以下n行描述该方格。金币数保证是不超过1000的正整数。
输出格式
　　最多能拿金币数量。
样例输入
3
1 3 3
2 2 2
3 1 2
样例输出
11
数据规模和约定
　　n<=1000
'''

n = int(input())
m = []

for i in range(n):
    m.append(list(map(int,input().split())))

res = 0

dp = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    dp[0][i] = dp[0][i-1] + m[0][i]
    dp[i][0] = dp[i-1][0] + m[i][0]
    
for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + m[i][j]

print(dp[n-1][n-1])

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j],end='')
#     print('')
