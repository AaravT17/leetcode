class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set() # stores chars in the current substring
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                # shrink window until it no longer contains duplicate chars
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
