'''
2039-网络空闲时刻

输入：edges = [[0,1],[1,2]], patience = [0,2,1]
输出：8
解释：
0 秒最开始时，
- 数据服务器 1 给主服务器发出信息（用 1A 表示）。
- 数据服务器 2 给主服务器发出信息（用 2A 表示）。

1 秒时，
- 信息 1A 到达主服务器，主服务器立刻处理信息 1A 并发出 1A 的回复信息。
- 数据服务器 1 还没收到任何回复。距离上次发出信息过去了 1 秒（1 < patience[1] = 2），所以不会重发信息。
- 数据服务器 2 还没收到任何回复。距离上次发出信息过去了 1 秒（1 == patience[2] = 1），所以它重发一条信息（用 2B 表示）。

2 秒时，
- 回复信息 1A 到达服务器 1 ，服务器 1 不会再重发信息。
- 信息 2A 到达主服务器，主服务器立刻处理信息 2A 并发出 2A 的回复信息。
- 服务器 2 重发一条信息（用 2C 表示）。
...
4 秒时，
- 回复信息 2A 到达服务器 2 ，服务器 2 不会再重发信息。
...
7 秒时，回复信息 2D 到达服务器 2 。

从第 8 秒开始，不再有任何信息在服务器之间传输，也不再有信息到达服务器。
所以第 8 秒是网络变空闲的最早时刻。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-time-when-the-network-becomes-idle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


import collections
import queue


class Solution:
    def networkBecomesIdle(self,edges,patience)->int:
        num = len(patience) #总的服务器数目
        g = [[] for _ in range(num)]
        # 定义一个邻接矩阵，表示无向图的顶点之间的联通情况
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        print(g)
        vis = [False]*num
        vis[0] = [True]
        queue = collections.deque()
        queue.append(0)
        ans = 0 #表示最终结果
        dist = 1
        while queue: #BFS搜索
            for _ in range(len(queue)): #层序遍历，由第0个节点进行遍历
                node = queue.popleft() 
                for v in g[node]: #对每一层的各个元素的操作
                    if vis[v] : continue
                    vis[v] = True #记录已经遍历过的元素
                    queue.append(v) #节点入队
                    ans = max(ans,dist*2+1 + (dist*2-1)//patience[v] *patience[v]) 
                    print(v,ans)
            dist = dist + 1
        return ans

e = [[0,1],[1,2]]
p = [0,2,1]
s = Solution()
ans=s.networkBecomesIdle(edges=e,patience=p)
print(ans)
