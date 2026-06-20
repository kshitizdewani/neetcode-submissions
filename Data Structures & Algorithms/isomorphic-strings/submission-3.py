class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = 0
        s_to_t = dict()
        t_to_s = dict()
        while i < len(s):
            s_item, t_item = s[i], t[i]
            if (s_item in s_to_t and s_to_t[s_item] != t_item) or (t_item in t_to_s and t_to_s[t_item] != s_item):
                return False
            
            s_to_t[s_item] = t_item
            t_to_s[t_item] = s_item
            i +=1
        return True