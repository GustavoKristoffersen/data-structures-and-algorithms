# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        left_i, right_i = 0, len(nums) - 1
        while left_i <= right_i:
            middle_i = (left_i + right_i) // 2
            if target == nums[middle_i]:
                return middle_i
            elif target > nums[middle_i]:
                left_i = middle_i + 1
            else:
                right_i = middle_i - 1
        
        if right_i > left_i:
            return right_i
        return left_i