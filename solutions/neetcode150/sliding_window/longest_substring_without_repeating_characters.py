class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_len = 0
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            max_len = max(r - l + 1, max_len)
            chars.add(s[r])
        return max_len
        # Time: O(n), Space: O(n)
