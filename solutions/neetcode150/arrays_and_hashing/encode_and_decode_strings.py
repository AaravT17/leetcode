from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Need an unambiguous delimiter to signal where each string begins and ends
        # Idea: Use %<length>%, this allows us to know exactly how many characters to read for each string, and we
        # can always correctly read the length of the string since there is no % in the length
        res = []
        for s in strs:
            res.append(f"%{len(s)}%{s}")

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        len_str = 0
        i = 0
        while i < len(s):
            i += 1
            while s[i] != "%":
                len_str = (len_str * 10) + int(s[i])
                i += 1
            i += 1  # skip the second %
            res.append(s[i : i + len_str])
            i += len_str
            len_str = 0

        return res
