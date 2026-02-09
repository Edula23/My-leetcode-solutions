from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for k, v in dic.items():
            if v == 1:
                return s.index(k)
        return -1