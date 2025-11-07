class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        di = {}
        for c in s:
            if c not in di:
                di[c] = 0
            di[c] += 1
        for c in t:
            if c not in s or di[c] < t.count(c):
                return c