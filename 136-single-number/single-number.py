class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        di = {}
        for n in nums:
            if n not in di:
                di[n] =0
            di[n] += 1
        for k, v in di.items():
            if v == 1:
                return k