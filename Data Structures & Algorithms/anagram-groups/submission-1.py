from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict automatically creates an empty list if the key doesn't exist yet
        hash_master = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word))
            hash_master[word_sorted].append(word)

        return list(hash_master.values())