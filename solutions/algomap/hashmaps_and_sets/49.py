from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1
        # h = {}

        # for s in strs:
        #     sorted_word = ''.join(sorted(s))
        #     if sorted_word in h:
        #         h[sorted_word].append(s)
        #     else:
        #         h[sorted_word] = [s]

        # return [h[key] for key in h]
        # The issue with this approach is that sorting each word is
        # unnecessary and inefficient, we can instead use a frequency
        # table (note that the frequency table must be of an immutable
        # type in order to be used as a key in the hashmap)

        # Approach 2
        h = {}

        for s in strs:
            freq_table = [0] * 26

            for char in s:
                freq_table[ord(char) - ord('a')] += 1

            key = tuple(freq_table)

            if key in h:
                h[key].append(s)
            else:
                h[key] = [s]

        return [h[key] for key in h]
