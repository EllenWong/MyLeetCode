'''
问题描述
　　给定一个1～N的排列a[i]，每次将相邻两个数相加，得到新序列，再对新序列重复这样的操作，显然每次得到的序列都比上一次的序列长度少1，最终只剩一个数字。
　　例如:
　　3 1 2 4
　　4 3 6
　　7 9
　　16
　　现在如果知道N和最后得到的数字sum，请求出最初序列a[i]，为1～N的一个排列。若有多种答案，则输出字典序最小的那一个。数据保证有解。
输入格式
　　第1行为两个正整数n，sum
输出格式
　　一个1～N的一个排列
样例输入
4 16
样例输出
3 1 2 4
数据规模和约定
　　0<n<=10
'''


import itertools


# def judge(mylist,len):
#     res = [[0 for i in range(len)] for j in range(len)]
#     for i in range(len):
#         res[0][i] = mylist[i]
#     for i in range(1,len):
#         for j in range(len - i):
#             res[i][j] = res[i-1][j] + res[i-1][j+1]
#     if len<1:
#         return 0
#     return res[len-1][0]


def last_row(row):
    res = [[0 for i in range(n)] for j in range(n)] #定义一个n行n列的数组，初始化为0
    for i in range(row):
        res[i][0] = 1
        res[i][i] = 1
        if i > 1:
            for j in range(1,i):
                res[i][j] = res[i-1][j] + res[i-1][j-1]
    return res[row-1]

# ls = [3,1,2]
# print(judge(ls,3))
n,sum = map(int,input().split())
used = [0 for i in range(n+2)]
result = []
flag = 0
row = last_row(n)

def dfs(num, t_sum):
    global flag
    if flag == 1:
        return
    if t_sum > sum:
        return
    if num == n: # 搜索到了序列中最后一个数字
        if t_sum == sum: #恰好此时结果为sum
            for x in result:
                print(x,'',end = '')
            flag =1
        else:
            return
    for i in range(1,n+1):
        if used[i]==0:
            used[i]=1
            result.append(i)
            dfs(num+1,t_sum + row[num]*i)
            used[i]=0
            result.pop()

if n==1:
    print(sum)
else:
    dfs(0,0)
