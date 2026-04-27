from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div(a, b):
            quotient = a / b
            if quotient < 0:
                return math.ceil(quotient)
            else:
                return math.floor(quotient)

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': div,
        }

        vals = []

        for token in tokens:
            if token in ops:
                b = vals.pop()
                a = vals.pop()
                vals.append(ops[token](a, b))
            else:
                vals.append(int(token))

        return vals[0]
