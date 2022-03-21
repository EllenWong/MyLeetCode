'''
题目描述
用筛法求之N内的素数。
输入
N
输出
0～N的素数
样例输入
100
样例输出
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
'''

n = int(input())

for i in range(2,n):
    for z in range(2,i):
        if i%z==0:
            break
    else:
        print(i,end='\n')
