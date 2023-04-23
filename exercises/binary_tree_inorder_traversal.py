# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root):
        arr = []
        def traverse(node):
            if node:
                traverse(node.left)
                arr.append(node.val)
                traverse(node.right)
        traverse(root)
        return arr
