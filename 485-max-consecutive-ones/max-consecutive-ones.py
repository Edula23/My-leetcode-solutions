class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxl = 0
        for n in nums:
            if n == 1:
                count += 1
                maxl = max(maxl, count)
            else:
                maxl = max(maxl, count)
                count = 0
        return maxl