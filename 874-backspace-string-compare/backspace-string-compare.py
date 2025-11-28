class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for i in range(len(s)):
            if s[i] == '#':
                if not s1:
                    continue
                s1.pop()
            else:
                s1.append(s[i])
        for i in range(len(t)):
            if t[i] == '#':
                if not t1:
                    continue
                t1.pop()
            else:
                t1.append(t[i])
        if s1 == t1:
            return True
        else:
            return False
        
           



        
