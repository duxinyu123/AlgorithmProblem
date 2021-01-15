# https://leetcode-cn.com/problems/linked-list-cycle/
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 1 快慢指针，快指针一次走两步 慢指针一次走一步, 若最终两指针相遇，则证明有环
    # 时间 O(n) 空间 O(1)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast, slow = head.next, head

        while fast != slow and fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            slow = slow.next

        if not fast:
            return False

        return True



