class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        i = 0
        con = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                con += 1
                i += 1
                j += 1
            else:
                i +=1 
        return con

            