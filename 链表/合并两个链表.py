# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnbp2/
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 1 迭代算法：子问题与原问题具有相同结构 时间：O(m+n) 空间：O(m+n)
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    # 2.迭代算法
    # 设定一个哨兵节点 prehead ，这可以在最后让我们比较容易地返回合并后的链表。
    # 我们维护一个 prev 指针，我们需要做的是调整它的 next 指针
    # 时间：O(m+n) 空间：O(1)
    def mergeTwoLists1(self, l1, l2):
        head = ListNode(-1, None)
        pre = head
        i = l1
        j = l2
        if not l1:
            return l2
        elif not l2:
            return l1

        while i and j:
            if i.val <= j.val:
                pre.next = i
                pre = i
                i = i.next
            else:
                pre.next = j
                pre = j
                j = j.next
        if not i:
            pre.next = j
        else:
            pre.next = i
        return head.next

