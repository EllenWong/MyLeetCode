import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur:
                q.append(cur.left)
                q.append(cur.right)
                res.append(str(cur.val))
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]": return 
        vals, i = data[1:-1].split(',') , 1
        q = collections.deque()
        root = TreeNode(int(vals[0]))
        q.append(root)
        while q:
            cur = q.popleft()
            if vals[i] != "null":
                cur.left = TreeNode(int(vals[i]))
                q.append(cur.left)
            i += 1
            if vals[i] != "null":
                cur.right = TreeNode(int(vals[i]))
                q.append(cur.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))