class Solution:
    def triangleType(self, nums: List[int]) -> str:
        res = ""
        for n in nums:
            if nums.count(n) == 3:
                return "equilateral"
            elif sum(nums) - n <= n:
                return "none"
        for n in nums:
            if nums.count(n) == 2:
                return "isosceles"
        return "scalene"

        
        