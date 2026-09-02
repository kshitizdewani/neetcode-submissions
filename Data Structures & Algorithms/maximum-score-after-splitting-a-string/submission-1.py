class Solution:

    def maxScore(self, s: str) -> int:
        prefix_map = dict()
        sum = 0
        for index, item in enumerate(s):
            if item == '1' :
                sum += 1
            prefix_map[index] = sum
        
        max_score = 0

        # len(s)-1 because right substring should never be empty
        for index in range(len(s) - 1):
            length_till_index = index+1
            ones_till_index = prefix_map[index]
            # left score
            left_zeroes = length_till_index - ones_till_index
            right_ones = prefix_map[len(s) - 1] - prefix_map[index]
            if left_zeroes + right_ones > max_score :
                max_score = left_zeroes + right_ones
        
        return max_score