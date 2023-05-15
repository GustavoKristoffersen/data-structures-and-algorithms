class Node:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = None
    
    # O(K)
    def insert(self, word):
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = Node()
                current_node.children[char] = new_node
                current_node = new_node
        current_node.children['*'] = None
        return self

    # O(K)
    def search(self, word):
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node


