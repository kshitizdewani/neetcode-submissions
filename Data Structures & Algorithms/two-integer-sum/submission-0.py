class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i,v in enumerate(nums):
            compliment = target - v
            # check if current number is any previous number's complement
            if v in hash:
                j = hash.get(v)
                return [j, i]
            hash[compliment] = i