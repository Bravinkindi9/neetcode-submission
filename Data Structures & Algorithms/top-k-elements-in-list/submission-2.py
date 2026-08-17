class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1
        sorted_nums = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        return sorted_nums[:k]