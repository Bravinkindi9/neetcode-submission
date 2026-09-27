class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right =  len(heights) - 1
        best = 0

        while left<right:
            width = right - left
            current_height = min(heights[left], heights[right])
            water = width * current_height
            best = max(best, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best