class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Approach 1
        # n = len(s)
        # chars = {}
        # most_freq = None
        # l = 0
        # longest = 0

        # for r in range(n):
        #     chars[s[r]] = chars.get(s[r], 0) + 1

        #     if chars[s[r]] >= chars.get(most_freq, 0):
        #         most_freq = s[r]

        #     while ((r - l) + 1) - chars.get(most_freq, 0) > k:
        #         chars[s[l]] -= 1
        #         l += 1
        #         most_freq = max(chars, key=chars.get)

        #     longest = max(longest, (r - l) + 1)

        # return longest

        # Approach 2
        # Use an array to track frequencies rather than a hashmap
        n = len(s)
        counts = [0] * 26
        l = 0
        longest = 0

        for r in range(n):
            counts[ord(s[r]) - 65] += 1
            while ((r - l) + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, (r - l) + 1)

        return longest
