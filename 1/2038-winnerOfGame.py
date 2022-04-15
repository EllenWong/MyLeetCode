'''
总共有 n 个颜色片段排成一列，每个颜色片段要么是 'A' 要么是 'B' 。给你一个长度为 n 的字符串 colors ，其中 colors[i] 表示第 i 个颜色片段的颜色。

Alice 和 Bob 在玩一个游戏，他们 轮流 从这个字符串中删除颜色。Alice 先手 。

如果一个颜色片段为 'A' 且 相邻两个颜色 都是颜色 'A' ，那么 Alice 可以删除该颜色片段。Alice 不可以 删除任何颜色 'B' 片段。
如果一个颜色片段为 'B' 且 相邻两个颜色 都是颜色 'B' ，那么 Bob 可以删除该颜色片段。Bob 不可以 删除任何颜色 'A' 片段。
Alice 和 Bob 不能 从字符串两端删除颜色片段。
如果其中一人无法继续操作，则该玩家 输 掉游戏且另一玩家 获胜 。
假设 Alice 和 Bob 都采用最优策略，如果 Alice 获胜，请返回 true，否则 Bob 获胜，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution: #记录连续的a与b的数值
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        tmp = 0
        for i in range(len(colors)):
            if colors[i] == 'A': tmp = tmp + 1
            else: tmp = 0
            a = a + max(0,tmp-2)
        if a == 0: return False
        #print(a)
        tmp = 0
        for i in range(len(colors)):
            if colors[i] == 'B': tmp = tmp + 1
            else: tmp = 0
            b = b + max(0,tmp-2)
        if a > b: return True
        else: return False