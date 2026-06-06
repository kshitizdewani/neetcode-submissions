class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenItems = []
        for i in nums :
            if i in seenItems:
                return True
            else:
                seenItems.append(i)
        
        return False
        