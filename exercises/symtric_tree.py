# https://leetcode.com/problems/symmetric-tree/submissions/938538232/

class Solution:
    def isSymmetric(self, root):
        def traverse(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return traverse(left.left, right.right) and traverse(left.right, right.left)
        return traverse(root.left,root.right)