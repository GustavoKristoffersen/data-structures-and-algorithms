# https://leetcode.com/problems/climbing-stairs/submissions/938121757/

class Solution:
    def climbStairs(self, n, hash={}):
        if n <= 3: return n
        if not hash.get(n):
            hash[n] = self.climbStairs(n - 1, hash) + self.climbStairs(n - 2, hash)
        return hash[n]