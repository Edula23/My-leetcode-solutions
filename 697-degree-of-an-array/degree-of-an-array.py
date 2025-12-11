class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        di = {}
        maxV = 0
        maxl = 0
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]] = 0
            di[nums[i]] += 1
            if di[nums[i]] > maxl:
                maxl= di[nums[i]]
                maxV = nums[i]
        maxValues = []
        for key, value in di.items():
            if value == maxl:
                maxValues.append(key)
        minLength = float('inf')        
        for maxV in maxValues:
            found = False
            i = 0
            j = len(nums) - 1
            while not found:
                if nums[i] == maxV and nums[j] == maxV:
                    found = True
                    minLength = min(minLength, j-i + 1)
                elif nums[i] != maxV and nums[j] != maxV:
                    i += 1
                    j -= 1
                elif nums[i] != maxV:
                    i += 1
                elif nums[j] != maxV:
                    j -= 1
        return minLength
 
