# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root):
        def bfs_count(root=None):
            if root is None:
                return 0
            
            levels = 1
            
            root.level = 1
            queue = [root]

            while len(queue) > 0:
                cur_node = queue.pop(0)

                levels = cur_node.level

                if cur_node.left is not None:
                    cur_node.left.level = cur_node.level + 1
                    queue.append(cur_node.left)

                if cur_node.right is not None:
                    cur_node.right.level = cur_node.level + 1
                    queue.append(cur_node.right)
            
            return levels

        return bfs_count(root)
