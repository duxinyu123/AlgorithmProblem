# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn7ihv/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 1. 中序遍历存放到数组中，判断该数组是否对称
    # 此情况可能存在问题 例如：[1,2,2,null,2], 优化方法，可以在append时，加上层级的数目
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = []
        self.in_travel(root, l, 0)
        if len(l) < 2:
            return True
        for i in range(len(l)//2):
            if l[i] != l[len(l)-1-i]:
                return False
        return True

    def in_travel(self, root, l, level):
        if not root:
            return
        self.in_travel(root.left, l, level+1)
        l.append(root.val+level)
        self.in_travel(root.right, l, level+1)

    # 2. 力扣答案： 深度周游
    # 判断左右镜像节点是否相同
    # 判断条件：1.左右子树的根是否相同 2.左右子树的左右子树是否对称
    def isSymmetric1(self, root):
        if not root:
            return True
        return self.deep_travel(root.left, root.right)

    def deep_travel(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.deep_travel(left.left, right.right) and self.deep_travel(right.left, left.right)

    # 3. 力扣答案：广度周游
    # 利用队列 将对称节点依次放入，然后两两取出比较
    def isSymmetric2(self, root):
        if not root:
            return True
        q = []
        q.append(root)
        q.append(root)
        while len(q) > 1:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if t1 and t2:
                if t1.val != t2.val:
                    return False
                q.append(t1.left)
                q.append(t2.right)
                q.append(t1.right)
                q.append(t2.left)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
        return True
