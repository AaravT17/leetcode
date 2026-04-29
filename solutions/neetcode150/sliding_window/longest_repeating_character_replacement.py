class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # in any given window, # replacements needed is the window length - # occurrences of most
        # frequently occurring character
        max_len = 0
        freq = [0] * 26  # counts the frequencies of characters in the substring
        l = 0
        for r in range(len(s)):
            # include the new character (at index r) in the window
            freq[ord(s[r]) - 65] += 1
            # while the window is invalid, shrink window and remove characters from the left
            while (r - l + 1) - max(freq) > k:
                freq[ord(s[l]) - 65] -= 1
                l += 1
            # we now have a valid window
            max_len = max(r - l + 1, max_len)
        return max_len
        # Time: O(n), Space: O(1)
