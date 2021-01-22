# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnldjj/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 利用队列广度优先遍历
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        q = []
        q.append(root)
        while len(q) > 0:
            cur_l = []
            num = len(q)
            for i in range(num):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                cur_l.append(cur.val)
            result.append(cur_l)
        return result



