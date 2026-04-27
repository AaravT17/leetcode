from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Need an unambiguous delimiter to signal the beginning and/or ending of each string
        # Idea: Use %<length>%
        res = []
        for s in strs:
            res.append(f"%{len(s)}%{s}")

        return "".join(res)

    def decode(self, msg: str) -> List[str]:
        res = []
        len_str = 0
        i = 0
        while i < len(msg):
            i += 1
            while msg[i] != "%":
                len_str = (len_str * 10) + int(msg[i])
                i += 1
            i += 1
            res.append(msg[i : i + len_str])
            i += len_str
            len_str = 0

        return res
