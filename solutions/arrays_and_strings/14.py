from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Approach 1
        # prefix = strs[0]  # bound to exist, strs.length >= 1
        # common_chars = len(prefix)

        # for s in strs:
        #     i = 0
        #     while i < min(len(s), common_chars) and s[i] == prefix[i]:
        #         i += 1

        #     if i == 0:
        #         return ''

        #     common_chars = i

        # return prefix[0:common_chars]

        # Approach 2
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[0:i]
            i += 1

        return strs[0][0:i]
