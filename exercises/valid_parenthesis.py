# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']': '['}
        openings = map.values()
        arr = []
        for char in s:
            if char in openings:
                arr.append(char)
            else:
                if not arr or arr.pop() != map.get(char):
                    return False

        return True if not arr else False