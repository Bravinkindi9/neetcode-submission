class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts= {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1  #starts the count dictionary from 0, then counts it and stores in some set, and then continues to another number

        sorted_items = sorted(counts.items(), key = lambda pair: pair[1], reverse = True) 
        
            #gives you the number-count pairs, lambda tells sorted "rank these by the count, the second thing in each pair, not the number itself and reverse means biggest count first instead of Python's default smallest-first

        top_k = sorted_items[:k]
        return [num for num, count in top_k]