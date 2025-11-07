class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        res = 0
        res, low, high = 0, 0, x - 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid < x:
                low = mid + 1
                res = mid
            elif mid * mid > x:
                high = mid - 1
            elif mid * mid == x:
                return mid
        return res
        