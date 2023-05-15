# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head):
        cur, prev = head, None
        while cur is not None:
            next = cur.next
            cur.next = prev
            cur, prev = next, cur
        return prev


class Solution:
    def reverseList(self, head, prev=None):
        if head is None:
            return prev
        next = head.next
        head.next = prev
        return self.reverseList(next, head)
        