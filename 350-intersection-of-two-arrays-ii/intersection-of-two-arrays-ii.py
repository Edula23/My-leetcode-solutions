class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di = {}
        res = []
        for i in nums1:
            if i not in di:
                di[i] = 0
            di[i] += 1
        for i in nums2:
            if i in di and di[i] > 0:
                res.append(i)
                di[i] -= 1
        return res