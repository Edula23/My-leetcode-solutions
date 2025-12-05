class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        noPart = 0
        total = 0
        for i in nums:
            total += i
        right = total
        left = 0
        for n in range(len(nums)-1):
            right += nums[n]
            left -= nums[n]
            if (left - right) % 2 == 0:
                noPart += 1
        return noPart 