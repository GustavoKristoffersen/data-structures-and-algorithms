# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, arr, target):
        seen = {}
        for index, num in enumerate(arr):
            remaining = target - num
            if remaining in seen:
                return [seen.get(remaining), index]
            seen[num] = index