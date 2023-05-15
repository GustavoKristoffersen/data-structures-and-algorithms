# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums):
        count = 0
        for num in nums:
            if num == 0: count += 1
        
        i = 0
        while count > 0:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count -= 1
            if nums[i] != 0:
                i += 1