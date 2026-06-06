class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        hash_s = dict()
        hash_t = dict()

        # Refactored loop for string s
        for v in s:
            hash_s[v] = hash_s.get(v, 0) + 1

        # Refactored loop for string t
        for v in t:
            hash_t[v] = hash_t.get(v, 0) + 1
            
        return hash_s == hash_t        