class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c = 1
        i = 0
        r = 1
        arrr = []
        while c <= k:
            if r not in arr:
                arrr.append(r)
                c+=1
                r+=1
            else:
                r+=1
        return arrr[-1]