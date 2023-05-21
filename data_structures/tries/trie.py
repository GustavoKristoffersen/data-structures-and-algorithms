class Node:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()
    
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
    
    def _collect_all_words(self, node=None, word='', words=[]):
        current_node = node or self.root
        for char, child_node in current_node.children.items():
            if char == '*':
                words.append(word)
            else:
                self._collect_all_words(child_node, word + char, words)
        return words

    def auto_complete(self, word):
        current_node = self.search(word)
        if not current_node:
            return []
        return self._collect_all_words(current_node)

    def auto_correct(self, word):
        word_found = ''
        current_node = self.root
        for char in word:
            if char in current_node.children:
                word_found += char
                current_node = current_node.children[char]
            else:
                possible_words = self._collect_all_words(current_node)
                if possible_words:
                    return word_found + possible_words[0]
                return possible_words
        return word

