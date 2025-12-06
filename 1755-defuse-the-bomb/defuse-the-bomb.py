class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        if k > 0:
            val = 0
            for i in range(len(code)):
                if i == len(code) - 1:
                    j = 0
                else:                
                    j = i + 1
                for x in range(k):
                    val+=code[j]
                    j += 1
                    if j > len(code)-1:
                        j = 0
                res.append(val)
                val = 0
            return res
        elif k < 0:
            k = -k
            val = 0
            for i in range(len(code)):
                if i == 0:
                    j = len(code) - 1
                else:                
                    j = i - 1
                for x in range(k):
                    val+=code[j]
                    j -= 1
                    if j < 0:
                        j = len(code) - 1
                res.append(val)
                val = 0
            return res
        elif k == 0:
            for i in range(len(code)):
                res.append(0)
            return res


