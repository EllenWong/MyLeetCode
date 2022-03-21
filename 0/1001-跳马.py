'''
问题描述
　　一个8×8的棋盘上有一个马初始位置为(a,b)，他想跳到(c,d)，问是否可以？如果可以，最少要跳几步？
输入格式
　　一行四个数字a,b,c,d。
输出格式
　　如果跳不到，输出-1；否则输出最少跳到的步数。
样例输入
1 1 2 3
样例输出
1
数据规模和约定
　　0<a,b,c,d≤8且都是整数。
'''

a,b,c,d = map(int,input().split())

min_step = float('inf')

dir = [[1,2],[1,-2],[2,1],[-2,1],[-2,-1],[2,-1],[-1,-2],[-1,2]]
visited = [[0 for i in range(9)] for _ in range(9)]
# print(visited)
visited[a][b] = 1

def dfs(x,y,step):
    global min_step
    global visited
    if step >= min_step: # 当前步数比最小步数大或者相等时
        #print(step,min_step)
        return 
    if x == c and y == d: # 当走到了指定位置时定义最小步数，并返回结果
        min_step = step
        return
    for i in range(8):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx,ny,step+1)
                visited[nx][ny] = 0
    
dfs(a,b,0)

if min_step == float('inf'):
    print('-1')
else:
    print(min_step)
