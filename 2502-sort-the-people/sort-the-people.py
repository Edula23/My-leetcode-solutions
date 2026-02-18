class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for h in range(len(heights)):
            for i in range(len(heights)):
                if heights[h] > heights[i]:
                    heights[h], heights[i] = heights[i], heights[h]
                    names[h], names[i] = names[i], names[h]
        return names




            
        