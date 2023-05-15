# https://leetcode.com/problems/top-k-frequent-elements/


class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for num, count in hashmap.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
