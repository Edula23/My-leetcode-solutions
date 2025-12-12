class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        digits[-1] +=1
        i = -1        
        while digits[i] > 9 and -(i-1) <= len(digits):
            digits[i] = 0
            if digits[i-1] == 9 and -(i-1)== len(digits):
                digits.append(0)
                digits[0] = 1
                return digits                
            digits[i-1] += 1
            i -= 1
        return digits