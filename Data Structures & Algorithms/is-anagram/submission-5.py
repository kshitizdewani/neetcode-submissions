class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        hash_s = dict()
        hash_t = dict()
        for i,v in enumerate(s):
            if v in hash_s:
                hash_s[v] += 1
                continue
            hash_s[v] = 1

        for i,v in enumerate(t):
            if v in hash_t:
                hash_t[v] += 1
                continue
            hash_t[v] = 1
        return hash_s == hash_t        