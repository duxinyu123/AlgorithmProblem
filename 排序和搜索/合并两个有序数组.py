# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnumcr/
class Solution(object):
    # 1. 把nums2放在num1尾部为0 的位置，然后在进行插入排序
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for i in range(0, n):
            nums1[i+m] = nums2[i]

        # 从m位置进行插入排序
        for i in range(m, m+n):
            for j in range(i, 0, -1):
                if nums1[j-1] > nums1[j]:
                    nums1[j-1], nums1[j] = nums1[j], nums1[j-1]
                else:
                    break
        return nums1

    # 2. 从后往前排序
    def merge1(self, nums1, m, nums2, n):
        pass
