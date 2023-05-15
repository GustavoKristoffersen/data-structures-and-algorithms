# https://leetcode.com/problems/linked-list-cycle/description/

# Floyd's Tortoise and Hare Algorithm
class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow == fast:
                return True
        return False