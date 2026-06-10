class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_master = dict()

        for i in strs:
            i_sorted = "".join(sorted(i))
            if i_sorted in hash_master:
                hash_master[i_sorted].append(i)
            else:
                hash_master[i_sorted] = [i]

        return list(hash_master.values())
