# https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        cur = slow
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        last = prev
        while last and head:
            if last.val != head.val:
                return False
            last = last.next
            head = head.next

        return True
