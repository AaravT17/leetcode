class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if n < m:
            return False

        # build a frequency table for s1, and maintain a frequency table for s2 for the current window of length m
        s1_freq, s2_freq = [0] * 26, [0] * 26
        for i in range(m):
            s1_freq[ord(s1[i]) - 97] += 1
            s2_freq[ord(s2[i]) - 97] += 1

        if s1_freq == s2_freq:
            return True

        # have to check fixed length windows of length m
        for i in range(n - m):
            s2_freq[ord(s2[i]) - 97] -= 1
            s2_freq[ord(s2[i + m]) - 97] += 1
            if s1_freq == s2_freq:
                return True

        return False
        # Time: O(n), Space: O(1)
