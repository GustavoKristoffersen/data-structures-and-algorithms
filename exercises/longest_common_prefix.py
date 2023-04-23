# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs_arr):
        strs_arr = sorted(strs_arr)
        first = strs_arr[0]
        last = strs_arr[-1]
        prefix = ''
        for i in range(len(first)):
            if first[i]!= last[i]:
                break
            prefix += first[i]
        return prefix

            
