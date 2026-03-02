class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            res[i] = summ
        return res

       