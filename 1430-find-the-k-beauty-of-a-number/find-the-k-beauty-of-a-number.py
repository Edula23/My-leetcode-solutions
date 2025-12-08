class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numStr = str(num)
        count = 0
        for i in range(len(numStr)-k+1):
            j = i + k
            val = int(numStr[i:j])
            if val != 0 and num % val == 0:
                count += 1
        return count