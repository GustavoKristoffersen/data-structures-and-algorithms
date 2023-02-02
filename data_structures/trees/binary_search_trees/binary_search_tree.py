class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    # O(log N)
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return self
                current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return self
                current_node = current_node.right
            else:
                return self

    # O(log N)
    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def remove(self, value):
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Case 1: When deleting the root node
                if parent_node is None:
                    self.root = None
                
                # Case 2: When the node being deleted has no child, just simply delete it
                elif current_node.left is None and current_node.right is None:
                    if current_node.value < parent_node.value:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                
                # Case 3: If it has only a left child, plug that child in the spot where the node being deleted was
                elif current_node.left is not None and current_node.right is None:
                    if current_node.value < parent_node.value:
                        parent_node.left = current_node.left
                    else:
                        parent_node.right = current_node.left
                
                # Case 4: Or if it has only a right child, plug that child in the spot where the node being deleted was  
                elif current_node.right is not None and current_node.left is None:
                    if current_node.value < parent_node.value:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right = current_node.right
                
                # Case 5: When deleting a node with two children, replace the deleted node
                # with the successor node. The successor node is the child node whose 
                # value is the least of all values that are greater than the deleted node.
                else:
                    # To find the successor node isit the right child of the to-be-deleted value
                    # and then keep on visiting the left child of each subsequent child until
                    # there are no more left children. The bottom value is the successor node.
                    successor_node = current_node.right
                    parent_of_successor = current_node
                    while successor_node.left is not None:
                        parent_of_successor = successor_node
                        successor_node = successor_node.left

                    # If the successor node has a right child, take that child and turn
                    # it into the left child of the former parent of the successor node.
                    if successor_node.right is not None:
                        parent_of_successor.left = successor_node.right
                    
                    if current_node.value < parent_node.value:
                        parent_node.left = successor_node
                    else:
                        parent_node.right = successor_node
                    successor_node.left = current_node.left
                    successor_node.right = current_node.right
            return True
        return False