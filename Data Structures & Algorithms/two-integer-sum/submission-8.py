class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #dictionary(index and value)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return