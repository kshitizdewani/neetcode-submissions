class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Using Bayes moore voting algorithm
        - Similar to pegionhole principle
        '''
        count = 0
        candidate = None

        for item in nums:
            if count == 0:
                count += 1
                candidate = item
                continue

            if candidate == item:
                count += 1
            else:
                count -= 1
        
        return candidate
             
        