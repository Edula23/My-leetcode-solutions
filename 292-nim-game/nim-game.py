class Solution:
    def canWinNim(self, n: int) -> bool:
        res = [1, 2, 3]
        if n % 4 in res:
            return True 
        else:
            return False