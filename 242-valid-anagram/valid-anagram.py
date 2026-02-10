from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        di = Counter(s)
        if len(s) != len(t):
            return False
        for ch in t:
            if ch not in di or t.count(ch) != di[ch]  :
                return False
        return True
