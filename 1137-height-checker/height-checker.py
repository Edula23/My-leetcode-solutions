class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortH = [x for x in heights]
        sortH.sort()
        ans = 0
        for i in range(len(heights)):
            if sortH[i] != heights[i]:
                ans += 1
        return ans