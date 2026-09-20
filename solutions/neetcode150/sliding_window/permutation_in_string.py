class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Approach 1
        # m, n = len(s1), len(s2)
        # if n < m:
        #     return False
        
        # s1_freqs, s2_freqs = [0] * 26, [0] * 26 # s2_freqs tracks char freqs in current substring/window in s2
        # for i in range(m):
        #     s1_freqs[ord(s1[i]) - ord('a')] += 1
        #     s2_freqs[ord(s2[i]) - ord('a')] += 1
        
        # if s1_freqs == s2_freqs:
        #     return True
        
        # for i in range(n - m):
        #     # shift window, then check if the current window is a permutation of s1 i.e. if char freqs match
        #     s2_freqs[ord(s2[i]) - ord('a')] -= 1
        #     s2_freqs[ord(s2[i + m]) - ord('a')] += 1
        #     if s1_freqs == s2_freqs:
        #         return True

        # return False
        # Time: O(n), Space: O(1)

        # Approach 2
        m, n = len(s1), len(s2)
        if n < m:
            return False
        
        s1_freqs, s2_freqs = [0] * 26, [0] * 26 # s2_freqs tracks char freqs in current substring/window in s2
        for i in range(m):
            s1_freqs[ord(s1[i]) - ord('a')] += 1
            s2_freqs[ord(s2[i]) - ord('a')] += 1

        matches = sum(s1_freqs[i] == s2_freqs[i] for i in range(26))
        if matches == 26:
            return True
        
        for i in range(n - m):
            # shift window, then check if the current window is a permutation of s1 i.e. if matches == 26
            removed, added = ord(s2[i]) - ord('a'), ord(s2[i + m]) - ord('a')
            s2_freqs[removed] -= 1
            if s2_freqs[removed] + 1 == s1_freqs[removed]:
                matches -= 1
            elif s2_freqs[removed] == s1_freqs[removed]:
                matches += 1

            s2_freqs[added] += 1
            if s2_freqs[added] - 1 == s1_freqs[added]:
                matches -= 1
            elif s2_freqs[added] == s1_freqs[added]:
                matches += 1
            
            if matches == 26:
                return True

        return False
        # Time: O(n), but the constant factor is reduced as we do not need to compare the two freq arrays each time
        # Space: O(1)
