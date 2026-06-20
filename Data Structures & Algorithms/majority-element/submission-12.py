class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        1.sort the array
        2.get the middle element(floor value works)
        3.return it.
        '''
        nums.sort()
        return nums[len(nums) // 2]