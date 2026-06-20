class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        middle = math.ceil(len(nums)/2)

        half1_set = set(sorted_nums[:middle])
        half2_set = set(sorted_nums[middle:])

        print(middle, sorted_nums[:middle], sorted_nums[middle:])

        for item in half2_set:
            if item in half1_set:
                return item
        return list(half1_set)[0]