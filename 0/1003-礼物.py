'''
问题描述
　　JiaoShou在爱琳大陆的旅行完毕，即将回家，为了纪念这次旅行，他决定带回一些礼物给好朋友。
　　在走出了怪物森林以后，JiaoShou看到了排成一排的N个石子。
　　这些石子很漂亮，JiaoShou决定以此为礼物。
　　但是这N个石子被施加了一种特殊的魔法。
　　如果要取走石子，必须按照以下的规则去取。
　　每次必须取连续的2*K个石子，并且满足前K个石子的重量和小于等于S，后K个石子的重量和小于等于S。
　　由于时间紧迫，Jiaoshou只能取一次。
　　现在JiaoShou找到了聪明的你，问他最多可以带走多少个石子。
输入格式
　　第一行两个整数N、S。
　　第二行N个整数，用空格隔开，表示每个石子的重量。
输出格式
　　第一行输出一个数表示JiaoShou最多能取走多少个石子。
样列输入
　　8 3
　　1 1 1 1 1 1 1 1
样列输出
　　6
数据规模和约定
　　对于20%的数据：N<=1000
　　对于70%的数据：N<=100,000
　　对于100%的数据：N<=1000,000，S<=10^12，每个石子的重量小于等于10^9，且非负
'''


# --------------Wrong-------------------

n,s = map(int,input().split())
ls = list(map(int,input().split()))


def check(tmp):
    # 对于位置为i的石头，求它的前tmp个与后tmp个石子之和是不是满足条件（<=s）
    for i in range(tmp,n-tmp+1):
        if sum_left[i] - sum_left[i-tmp] <= s and sum_left[i+tmp] - sum_left[i] <=s:
            return True
    return False


# 求这n个数字的前缀和
sum_left = [0 for i in range(n+1)]
for i in range(1,n+1):
    sum_left[i] = sum_left[i-1] + ls[i-1]

print(sum_left)

# 用二分法的方式进行问题求解
l = 1
r = n
# mid = l+(r-1)>>1
# print(mid)

while(l<r):
    mid = l+(r+1)>>1
    print(mid)
    if check(mid):
        # print(mid)
        l = mid
        #break
    else:
        r = mid-1

print(2*l)


