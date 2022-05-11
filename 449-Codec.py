# Definition for a binary tree node.
from cmath import inf

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        def PostOrder(root):
            if root is None:
                return 
            PostOrder(root.left)
            PostOrder(root.right)
            arr.append(root.val)
        PostOrder(root)
        return ' '.join(map(str,arr))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = list(map(int, data.split())) #将字符串转变为列表
        def construct(lower,upper):
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower,val)
            return root
        return construct(-inf,inf)        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans