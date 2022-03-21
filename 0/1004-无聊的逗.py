'''
问题描述
　　逗志芃在干了很多事情后终于闲下来了，然后就陷入了深深的无聊中。不过他想到了一个游戏来使他更无聊。他拿出n个木棍，然后选出其中一些粘成一根长的，然后再选一些粘成另一个长的，他想知道在两根一样长的情况下长度最长是多少。
输入格式
　　第一行一个数n，表示n个棍子。第二行n个数，每个数表示一根棍子的长度。
输出格式
　　一个数，最大的长度。
样例输入
4
1 2 3 1
样例输出
3
数据规模和约定
　　n<=15
'''

def subsets(ls): #求列表的子集
    res = [[]]
    for num in ls:
        res += [[num] + x for x in res ]
    return res

def half_subsets(sub): #求等长子集(通过80%，会超时)
    total = sum(sub)
    target = total//2
    if total % 2 == 1:
        return False,target

    if max(sub) > target:
        return False,target
    
    n = len(sub)
    if n < 2:
        return False,target

    dp = [[False] * (target + 1) for _ in range(n)] # dp[i][j]表示下标(0,i)中，子集的和恰好为j，是否存在
    
    for i in range(n):
        dp[i][0] = True

    dp[0][sub[0]] = True

    for i in range(1,n):
        for j in range(1,target+1):
            if j<sub[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-sub[i]] or dp[i-1][j]

    return dp[n-1][target],target


def half_subsets2(sub): #通过100%
    total = sum(sub)
    target = total//2
    if total % 2 == 1:
        return False,target

    if max(sub) > target:
        return False,target

    n = len(sub)
    if n < 2:
        return False,target #特殊情况下的输出


    L = [True] + [False] * target #一个长度为target + 1的数组，L[target]表示对于sub而言，是否有子集和为target，显然，L[0]表示空子集，和为0

    for num in sub: #num表示集合sub的元素
        for i in range(target, num - 1, -1): #i表示从targe 到 num - 1的index（递减）
            L[i] = L[i] or L[i - num]

    return L[-1],target

# ls = [1,2,3]

# print(half_subsets(ls))

n = int(input())
ls = list(map(int,input().split()))

subset = subsets(ls)

max_result = 0

for sub in subset:
    if not sub:
        continue
    flag, target = half_subsets(sub)
    if flag and target > max_result:
        max_result = target

print(max_result)