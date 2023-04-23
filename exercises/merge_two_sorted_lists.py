# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, head1, head2):
        m_head = ListNode()
        m_tail = m_head
        while head1 and head2:
            if head1.val <= head2.val:
                m_tail.next = head1
                head1 = head1.next
            else:
                m_tail.next = head2
                head2 = head2.next
            
            m_tail = m_tail.next

        if head1:
            m_tail.next = head1
        elif head2:
            m_tail.next = head2

        return m_head.next

            