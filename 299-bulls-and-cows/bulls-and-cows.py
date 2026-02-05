from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sc = Counter(secret)
        gc = Counter(guess)
        b = 0
        c = 0
        res = ""
        for i in range(len(secret)):
            if secret[i] == guess[i] :
                sc[secret[i]]-=1
                gc[guess[i]] -=1
                b+=1
        for i in range(len(secret)):   
            if secret[i] != guess[i]  and sc[guess[i]] > 0:
                c+=1
                sc[guess[i]]-=1
                gc[guess[i]] -=1
        res = str(b) + "A" + str(c) + "B"
        return res
