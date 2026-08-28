class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1 
        max_water = 0
        while l<r:
            width = r - l
            height = min(heights[l], heights[r])
            current_water = width * height
            max_water = max(max_water, current_water)

            if heights[l] < heights[r]:
                l +=1
            else:
                r-= 1
        return max_water