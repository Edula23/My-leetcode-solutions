class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res =[]
        for i in range(len(numbers)):
            low = i + 1
            high = len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] + numbers[i] < target:
                    low = mid + 1
                elif numbers[mid] + numbers[i] > target:
                    high = mid - 1
                else:
                    res.append(i+1)
                    res.append(mid+1)
                    return res
        return res
        
                    

        