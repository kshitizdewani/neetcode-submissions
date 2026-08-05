class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = {}
        stack = []
        
        for i, val in enumerate(nums2):
            while stack and stack[-1] < val:
                next_greater[stack.pop()] = val
            
            if val in nums1:
                stack.append(val)
        
        for leftover in stack :
            next_greater[leftover] = -1
        
        return [next_greater[item] for item in nums1]
