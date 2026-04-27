class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(
            s1
        )  # we must check fixed length substrings of length n1 in s2 to see if they are a permutation of s1
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_chars = {}
        substring_chars = {}

        for i in range(n1):
            s1_chars[s1[i]] = s1_chars.get(s1[i], 0) + 1
            substring_chars[s2[i]] = substring_chars.get(s2[i], 0) + 1

        if s1_chars == substring_chars:
            return True

        for i in range(n1, n2):
            if substring_chars[s2[i - n1]] == 1:
                del substring_chars[s2[i - n1]]
            else:
                substring_chars[s2[i - n1]] -= 1

            substring_chars[s2[i]] = substring_chars.get(s2[i], 0) + 1
            if s1_chars == substring_chars:
                return True

        return False
