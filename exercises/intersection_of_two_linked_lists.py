# https://leetcode.com/problems/intersection-of-two-linked-lists/

# My first solution
class Solution:
    def getIntersectionNode(self, headA, headB):
        a_len = 1
        b_len = 1
        a_node = headA
        b_node = headB
        while a_node.next is not None or b_node.next is not None:
            if a_node.next:
                a_len += 1
                a_node = a_node.next
            if b_node.next:
                b_len += 1
                b_node = b_node.next

        if a_node is not b_node:
            return None
        
        if a_len > b_len:
            while headA is not headB:
                if a_len == b_len:
                    headB = headB.next
                    b_len -= 1
                headA = headA.next
                a_len -= 1
        else:
            while headB is not headA:
                if b_len == a_len:
                    headA = headA.next
                    a_len -= 1
                headB = headB.next
                b_len -= 1
        
        return headA
    

# From solutions
class Solution:
    def getIntersectionNode(self, headA, headB):
        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one
