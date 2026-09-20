class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Approach 1
        # num replacements in substring = length of substring - max freq of any char in substring
        freqs = [0] * 26
        l = 0
        longest = 0
        for r in range(len(s)):
            freqs[ord(s[r]) - ord('A')] += 1 # include current char in window before we check validity
            while (r - l + 1) - max(freqs) > k:
                # window is invalid, shrink from left
                freqs[ord(s[l]) - ord('A')] -= 1
                l += 1
            # window is valid, check length and update longest if necessary
            longest = max(longest, r - l + 1)
        return longest
        # Time: O(n), Space: O(1)

        # Approach 2
        # Key insight: We do not need to track the exact max freq in the current substring. It is sufficient to track
        # the max freq we have seen in a valid substring at any point so far because we can only get a longer valid 
        # substring than the longest we have seen so far if we find a valid substring with a greater max freq. So, it 
        # is okay if we do not update the max freq tracker when we shrink the window as this cannot lead to a greater 
        # max freq. We need only update the tracker when we have (or may have) a greater value, and it is only  
        # possible to get a greater value when we expand the substring/window to the right. This new max can only be 
        # caused by the new char we added on the right, so to update the max freq, we need only check if the freq of 
        # the newly added char in the current substring > max freq and update max freq if it is. This means that the 
        # constant factor reduces as there is no need to compute max over an array of 26 elements. Note that we must
        # still accurately track the char freqs in the current substring, but this is a single increment/decrement 
        # each time we shrink/expand the window. The lazy update rule only applies to the max freq tracker, not to the
        # freqs of chars in the current substring. Essentially, the max freq tracker is an upper bound on the max freq
        # for the current substring, and it was equal to the max freq for some valid substring up to this point.
        # freqs = [0] * 26
        # l = 0
        # longest = 0
        # max_freq = 0  # holds the max freq of any char in a valid substring at any point so far
        # for r in range(len(s)):
        #     freqs[ord(s[r]) - ord('A')] += 1
        #     max_freq = max(max_freq, freqs[ord(s[r]) - ord('A')])
        #     while (r - l + 1) - max_freq > k:
        #         freqs[ord(s[l]) - ord('A')] -= 1
        #         l += 1
        #     longest = max(longest, r - l + 1)
        # return longest
        # Time: O(n), but the constant factor is reduced since we do not need to compute max(freqs) every time
        # Space: O(1)
