from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0 #should be greatest
        min_even = 101 #should be smallest
        freq_map = dict()

        # for element in s:
        #     frequency = freq_map.get(element, 0) + 1
        #     freq_map[element] = frequency
        # `--> Replaced by Counter


        for frequency in Counter(s).values():
            if frequency % 2 != 0:
                max_odd = max(frequency, max_odd)
            else:
                min_even = min(frequency, min_even)

        return max_odd - min_even