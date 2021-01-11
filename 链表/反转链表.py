# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnhm6/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution(object):
    # 1 递归方式实现
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        elif head.next:
            return self.reverse(head, head.next)
        else:
            return head

    def reverse(self, pre, nex):
        if nex:
            tail = self.reverse(nex, nex.next)
            nex.next = pre
            pre.next = None
        else:
            tail = pre
        return tail

    # 2 三指针实现
    def reverseList1(self, head):
        if not head:
            return None
        elif not head.next:
            return head
        elif not head.next.next:
            tail = head.next
            tail.next = head
            head.next = None
            return tail
        i,j,z = head, head.next, head.next.next
        i.next = None
        while z:
            j.next = i
            i = j
            j = z
            z = z.next
        j.next = i
        return j


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

s = Solution()
print(s.reverseList1(a))
