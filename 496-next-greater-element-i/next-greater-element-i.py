class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n2 = len(nums2)
        ans = [-1] * n2       # Stores next greater element for each index in nums2
        stack = []

        # Step 1: Precompute next greater elements for nums2
        for i in range(n2 - 1, -1, -1):  # Traverse from right to left
            # Pop elements from the stack smaller than or equal to current
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            # Top of the stack is the next greater element
            if stack:
                ans[i] = stack[-1]
            # Push current element to stack
            stack.append(nums2[i])

        # Step 2: Create the result for nums1 using precomputed values
        res = []
        for num in nums1:
            for j in range(n2):
                if nums2[j] == num:
                    res.append(ans[j])  # Get the precomputed next greater
                    break

        return res