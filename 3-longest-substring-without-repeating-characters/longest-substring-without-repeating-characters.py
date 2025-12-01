class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = mlength = 0 
        cSet = set()       
        for i in range(len(s)):
            while s[i] in cSet:
                cSet.remove(s[left])
                left += 1
            cSet.add(s[i])
            mlength = max(mlength, i - left + 1)
        return mlength
