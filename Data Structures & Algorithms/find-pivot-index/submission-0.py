class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        map = dict()
        sum = 0
        for i, item in enumerate(nums):
            sum += item
            map[i] = sum
        
        for i, item in enumerate(nums):
            left_sum = map[i] - item
            right_sum = map[len(nums) - 1] - map[i]
            if left_sum == right_sum :
                return i
        return -1