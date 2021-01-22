#https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnto1s/
def isBadVersion(version):
    pass
class Solution(object):
    # 1. 循环判断
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return
        if n == 1:
            return n
        left = 1
        right = n

        while left < right - 1:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return left if isBadVersion(left) else right

    # 2.递归判断
    def firstBadVersion1(self, n):
        def helper(l, r):
            if l == r-1:
                return l if isBadVersion(l) else r
            mid = (l + r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
            return helper(l, r)
        if n == 1:
            return n
        return helper(1, n)


