class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        i =0
        j= len(s) -1
        newStr = list(s)
        while i < j and i < len(s) and j > 0:
            if s[i].lower() not in vowels:
                i+= 1
            if s[j].lower() not in vowels:
                j-=1
            if s[i].lower() in vowels and s[j].lower() in vowels:                
                temp = newStr[i]
                newStr[i] = newStr[j]
                newStr[j] = temp
                i+=1
                j-=1
        return "".join(newStr)
