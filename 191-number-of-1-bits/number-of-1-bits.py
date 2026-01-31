class Solution:
    def hammingWeight(self, n: int) -> int:
        res = []
        while n >= 1:
            res.append(n%2)
            n = n // 2
        return res.count(1)
            