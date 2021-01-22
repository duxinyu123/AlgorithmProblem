# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xninbt/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 1. 采用二分法的思想,每次选取最中间的节点作为根
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        return self.build_tree(nums, 0, len(nums)-1)


    def build_tree(self, nums, left, right):
        if left > right:
            return
        elif left == right:
            return TreeNode(left)
        mid = len(left+right) // 2
        root = nums[mid]
        root.left = self.build_tree(nums, left, mid - 1)
        root.right = self.build_tree(nums, mid + 1, right)
        return root








