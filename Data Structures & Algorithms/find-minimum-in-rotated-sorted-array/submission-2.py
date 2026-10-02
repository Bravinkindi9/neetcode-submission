class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:   # we are not using an equal sign bcz we have nothing to compare with the target
            mid = (left + right) //2

            if nums[mid] > nums[right]: #here we have a way of 
                left = mid + 1
            else:
                right = mid
        return nums[left]