# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums):
        res, count = nums[0],1
        for i in range(1, len(nums)):
            if nums[i] == res:
                count += 1
            else:
                if count == 0:
                    res, count = nums[i], 1
                count -= 1
        return res