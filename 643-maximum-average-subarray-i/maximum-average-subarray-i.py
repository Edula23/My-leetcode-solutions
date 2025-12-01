class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        for i in range(k):
            summ += nums[i]
        maxSum = summ
        for i in range(len(nums)-k):
            summ -= nums[i]
            summ += nums[i+k]
            maxSum = max(maxSum, summ)
        return maxSum/k
        # left = 0
        # right = left + k
        # maxAv = 0
        # if len(nums) <= 1:
        #     return nums[0]/k
        # while right <= len(nums):
        #     summ = 0
        #     for i in range(left, right):
        #         summ += nums[i]
        #     average = summ/k
        #     maxAv = max(maxAv, average)
        #     left += 1
        #     right += 1
        # return maxAv