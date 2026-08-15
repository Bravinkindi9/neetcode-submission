class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)==1): return [strs]
        words = {}
        for w in strs:
            form = "".join(sorted(w))
            if form not in words:
                words[form] = [w]
            else:
                words[form].append(w)
        return list(words.values())  