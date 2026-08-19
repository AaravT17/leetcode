from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap: dict[tuple[int], List[str]] = {}  # char freq tuple -> list of strings

        for s in strs:
            freqs = [0] * 26
            for char in s:
                freqs[ord(char) - ord('a')] += 1
            freq_tuple = tuple(
                freqs
            )  # lists cannot be used as keys in a hashmap since they are mutable, but tuples can since they are immutable
            if freq_tuple in hashmap:
                hashmap[freq_tuple].append(s)
            else:
                hashmap[freq_tuple] = [s]

        return [list_strs for list_strs in hashmap.values()]
