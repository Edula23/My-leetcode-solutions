class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = m
        for i in nums2:
            nums1[a] = i
            a+=1
        return nums1.sort()

                    

        """
        Do not return anything, modify nums1 in-place instead.
        """
        