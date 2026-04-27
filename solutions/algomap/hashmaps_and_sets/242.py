from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach 1
        # if len(s) != len(t):
        #     return False

        # s_chars = {}
        # for char in s:
        #     if char in s_chars:
        #         s_chars[char] += 1
        #     else:
        #         s_chars[char] = 1

        # for char in t:
        #     if char not in s_chars:
        #         return False
        #     elif s_chars[char] == 1:
        #         del s_chars[char]
        #     else:
        #         s_chars[char] -= 1

        # return True
        # Since we checked whether the lengths of s and t are equal at the
        # beginning, we can guarantee that if we make it out of the loop,
        # s_chars must be empty, and therefore s and t are anagrams, if that
        # initial check had not been present, the return statement would be
        # return not s_chars to ensure that s does not have any extra
        # characters that are not in t

        # Approach 2
        if len(s) != len(t):
            return False

        # Compare the frequency tables for s and t, if they are equal,
        # then they are anagrams
        return Counter(s) == Counter(t)
