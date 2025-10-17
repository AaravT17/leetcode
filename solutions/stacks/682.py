from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op == 'C':
                scores.pop()
            elif op == 'D':
                scores.append(int(scores[-1]) * 2)
            elif op == '+':
                scores.append(int(scores[-1]) + int(scores[-2]))
            else:  # op is an integer
                scores.append(int(op))

        return sum(scores)
