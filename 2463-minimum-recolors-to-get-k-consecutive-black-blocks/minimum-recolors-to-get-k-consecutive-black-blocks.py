class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks) == 1:
            if blocks == "W":
                return 1
            else:
                return 0
        elif blocks.count("W") == len(blocks):
            return k
        left = 0
        right = 0 
        countB = 0
        for i in range(len(blocks)):
            j = i + k
            newArr = blocks[i:j]
            if newArr.count("B") > countB :
                countB = newArr.count("B")
                left = i
                right = j
        newArr = blocks[left:right]
        return newArr.count("W")