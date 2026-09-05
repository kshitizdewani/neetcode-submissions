class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_map = dict()
        sum = 0
        vowels = ['a','e','i','o','u']
        for i, val in enumerate(words):
            is_vowel = 0
            if val[0] in vowels and val[-1] in vowels:
                sum += 1
                is_vowel = 1
            prefix_map[i] = [sum, is_vowel]

        output = list()
        for query in queries :
            # 0 - i --> sum(i)
            if query[0] == 0:
                count = prefix_map[query[1]][0]
            # i - i --> is_vowel
            elif query[0] == query[1]:
                count = prefix_map[query[1]][1]
            # x - y --> sum(y) - sum(x-1)
            else :
                count = prefix_map[query[1]][0] - prefix_map[query[0] - 1][0]
            output.append(count)

        return output    