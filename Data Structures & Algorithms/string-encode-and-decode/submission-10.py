class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        return result

    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": 
                j +=1 #we count for 
            length = int(s[i:j])
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            i = end
        return decoded