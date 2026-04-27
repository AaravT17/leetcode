class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        chars = set()  # tracks the characters in the current substring
        l = 0
        longest = 0

        for r in range(n):
            while s[r] in chars:  # window is invalid, make it valid again
                chars.remove(s[l])
                l += 1

            # we have a valid window from L to R, inclusive
            chars.add(s[r])
            # update longest window
            longest = max(longest, (r - l) + 1)

        return longest
