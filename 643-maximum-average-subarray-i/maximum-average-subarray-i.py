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
       