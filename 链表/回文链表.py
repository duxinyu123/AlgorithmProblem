# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnv1oc/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 1 快慢指针法：时间复杂度O(n) 空间复杂度O(1)
    # 先遍历整个链表，得到链表长度length，
    # 然后根据length/2拿到中间指针，将后半部分链表指针反转
    # 拿到tail指针，while依次循环判断head.next 与tail.next是否全部相等
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        current = head
        while current:
            length = length + 1
            current = current.next

        if length < 2:
            return True
        elif length == 2:
            if head.val == head.next.val:
                return True
            else:
                return False

        current = head
        mid_index = int(length/2)

        i = 0
        while i < mid_index:
            current = current.next
            i = i + 1
        pre = current
        pre_p = current.next
        while pre_p:
            pre_p_p = pre_p.next
            pre_p.next = pre
            pre = pre_p
            pre_p = pre_p_p
            if pre_p_p:
                pre_p_p = pre_p_p.next

        tail = pre
        while head != tail and tail.next != head:
            if head.val != tail.val:
                return False
            else:
                head = head.next
                tail = tail.next
        return True

    # 2 hash法
    # 正向/反向求出链表的hash值，比较是否相等
    def isPalindrome2(self, head):
        pass





a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c

s = Solution()
print(s.isPalindrome(a))

