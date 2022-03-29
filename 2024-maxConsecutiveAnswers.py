'''
考试的最大困扰度

请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。 

示例 1：

输入：answerKey = "TTFF", k = 2
输出：4
解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。
总共有四个连续的 'T' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxChar(ch:str):
            ans = 0
            csum = 0
            left = 0
            for right in range(len(answerKey)): #更新滑动窗口右边界
                if answerKey[right] != ch:
                    csum = csum + 1
                while csum > k: #更新滑动窗口左边界
                    if answerKey[left] != ch:
                        csum = csum - 1
                    left = left + 1
                ans = max(ans,right-left+1)
            return ans

        return max(maxChar('T'),maxChar('F'))