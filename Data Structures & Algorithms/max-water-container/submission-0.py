class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0

        # while left<right:
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                length = min(heights[j],heights[i])
                max_water = max(max_water, width*length)


        return max_water