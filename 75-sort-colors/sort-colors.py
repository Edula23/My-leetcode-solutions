class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-2, -1, -1):
            for j in range(0, i+1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp

        """
        Do not return anything, modify nums in-place instead.
        """
        