class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = dict()
        for i in nums:
            if i in hash:
                return True
            else:
                hash[i] = 0
        return False