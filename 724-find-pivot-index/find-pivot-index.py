class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        leftS = 0
        rightS = 0
        for i in range(len(nums)):
            if i == 0:
                leftS = 0
                rightS = total - nums[i]
            elif i == len(nums) - 1:
                rightS = 0
                leftS = total - nums[len(nums)-1]
            else:
                leftS += nums[i-1]
                rightS -= nums[i]
            if rightS == leftS:
                return i
        return -1
        