# https://leetcode.com/problems/group-anagrams/

# my solution
# even though it has a worse time complexity, it still
# runs faster in the tests, probably because the strings
# are so short that the sorting does not take relevant time
class Solution(object):
    def groupAnagrams(self, strs):
        sor = {}
        for s in strs:
            key = ''.join(sorted(s))
            sor[key] = sor.get(key, []) + [s]
        
        return sor.values()

# optimal solution
class Solution(object):
    def groupAnagrams(self, strs):
        sor = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                key[index] += 1

            key = tuple(key)
            sor[key] = sor.get(key, []) + [s]            
        
        return sor.values()