from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dis = Counter(s)
        dit = Counter(t)
        if len(s) != len(t):
            return False
        for ch in t:
            # if ch not in di or t.count(ch) != di[ch]  :
            if dit[ch] != dis[ch]:
                return False
        return True
