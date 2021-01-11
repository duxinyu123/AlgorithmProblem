# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn2925/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 方式1： 计算链表长度，时间复杂度O()
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1
        current = head
        while current.next:
            current = current.next
            length = length + 1

        current = head
        i = 0
        n = length - n
        if n == 0:
            head = head.next
            current.next = None
            return head
        while current.next:
            if i == n - 1:
                break
            current = current.next
            i = i + 1

        after = current.next
        current.next = current.next.next
        after.next = None
        return head

    # 2.快慢指针 快慢指针相差n个节点，则当快指针到末尾时，慢指针为要删除节点的上一个节点 O(n)
    def removeNthFromEnd1(self, head, n):
        pre = head
        after = head
        pre_index = 0
        if head.next == None:
            return None
        while pre.next:
            pre = pre.next
            pre_index = pre_index + 1
            if pre_index > n:
                after = after.next
        if pre_index + 1 == n:
            head = head.next
        else:
            after.next = after.next.next
        return head








