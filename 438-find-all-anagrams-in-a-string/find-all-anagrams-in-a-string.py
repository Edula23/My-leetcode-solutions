class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = Counter(p)
        countWindow = Counter()
        res = []
        left = 0
        if len(p) > len(s):
            return []
        for i in range(len(p)):
            countWindow[s[i]] +=1
        if countWindow == countP:
            res.append(0)

        for right in range(len(p), len(s)):
            print(left, right, countWindow)
            countWindow[s[right]] += 1
            countWindow[s[left]] -= 1
            if countWindow[s[left]] == 0:
                del countWindow[s[left]]    
            left+=1
            if countWindow == countP:
                res.append(left)
        return res                       