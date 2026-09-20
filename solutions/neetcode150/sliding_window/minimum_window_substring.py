class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(t), len(s)
        if m > n:
            return ''

        # a valid window is one where freq in current window in s >= freq in t for every char in t
        # we only care about freqs of chars that are in t, ignore chars not in t
        t_freq, s_freq = {}, {}  # s_freq tracks freq of relevant chars in current substring/window in s
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        matches, reqd_matches = 0, len(t_freq)
        shortest, start = n + 1, 0
        l = 0
        for r in range(n):
            if s[r] in t_freq:
                # char is relevant
                s_freq[s[r]] = s_freq.get(s[r], 0) + 1
                # adding chars can only increase num matches
                if s_freq[s[r]] == t_freq[s[r]]:
                    matches += 1

            while matches == reqd_matches:
                # window is valid, update shortest (if reqd.) and shrink window
                length = r - l + 1
                if length < shortest:
                    shortest, start = length, l
                if s[l] in t_freq:
                    s_freq[s[l]] -= 1
                    # removing chars can only reduce num matches
                    if s_freq[s[l]] + 1 == t_freq[s[l]]:
                        matches -= 1
                l += 1

        return s[start : start + shortest] if shortest <= n else ''
        # Time: O(n)
        # Space: O(1), since s, t consist of uppecase and lowercase english alphabets i.e. <= 52 distinct chars
