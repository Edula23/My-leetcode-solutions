class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0
        count = 0
        for i in range(2, len(s)):
            if s[i-1] != s[i] and s[i-2] != s[i] and s[i-1] != s[i-2]:
                count+=1
        return count
        