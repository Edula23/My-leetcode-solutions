class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxx = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > maxx:
                maxx = nums[i+1] - nums[i]
        return(maxx)

        