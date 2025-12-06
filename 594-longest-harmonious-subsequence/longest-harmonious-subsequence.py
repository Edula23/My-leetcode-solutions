class Solution:
    def findLHS(self, nums: List[int]) -> int:
        di = {}
        curl = 0
        maxl = 0
        for n in nums:
            if n not in di:
                di[n] = 0
            di[n] += 1
        for i in nums:
            if i + 1 in di:
                curl = di[i] + di[i+1]
            maxl = max(maxl, curl)
        return maxl