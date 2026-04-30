class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(t), len(s)
        if m < n:
            return ""

        # maintain a hashmap of chars in both strings
        # in s_set, only worry about counts of chars in t, the rest are irrelevant
        s_set, t_set = {}, {}
        distinct_chars = 0
        for char in t:
            if char not in t_set:
                distinct_chars += 1
            t_set[char] = 1 + t_set.get(char, 0)

        min_window_len = m + 1  # longer than any possible valid window in s
        min_window_start = 0
        # track how many of the distinct chars in t are contained (with reqd. min count) in the current window in s
        valid_chars = 0
        l = 0
        for r in range(m):
            # expand the window to the right
            if s[r] in t_set:
                s_set[s[r]] = 1 + s_set.get(s[r], 0)
                if s_set[s[r]] == t_set[s[r]]:  # we just hit the reqd. min count
                    valid_chars += 1
            while valid_chars == distinct_chars:
                # check if the window is the shortest valid window
                window_len = r - l + 1
                if window_len < min_window_len:
                    min_window_len = window_len
                    min_window_start = l
                # shrink the window
                if s[l] in t_set:
                    s_set[s[l]] -= 1  # if we are shrinking, then s[l] must be in s_set
                    if s_set[s[l]] + 1 == t_set[s[l]]:
                        # we just sunk below the reqd. min count
                        valid_chars -= 1
                l += 1

        if min_window_len > m:
            return ""
        return s[min_window_start : min_window_start + min_window_len]
        # Time: O(m), Space: O(1) (<= 52 distinct characters (only uppercase and lowercase english letters),
        # so <= 52 elements in each hashmap)
