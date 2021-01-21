# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn08xg/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #  1. 递归方法 判断当前root.val 是否在lower与upper之间
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 正无穷 float("inf"), 负无穷 float("-inf")
        def helper(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            flag = helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
            return flag

        return helper(root, float("-inf"), float("inf"))

    # 2. 中序遍历 中序遍历结果放在队列中，如果取出来不是递增序列，则不是二叉排序树
    def isValidBST1(self, root):
        q = []
        self.in_travel(root, q)
        if len(q) < 2:
            return True
        cur = q.pop(0)
        nt = q.pop(0)
        while cur is not None and nt is not None:
            if cur < nt:
                cur = nt
                if len(q) > 0:
                    nt = q.pop(0)
                else:
                    nt = None
            else:
                return False
        return True

    def in_travel(self, root, q):
        if not root:
            return
        self.in_travel(root.left, q)
        q.append(root.val)
        self.in_travel(root.right, q)





