class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        mustbeone = False
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            elif i == len(bits)-1 and bits[i] == 0:
                mustbeone = True
                break
            else:
                i += 1
        return mustbeone
