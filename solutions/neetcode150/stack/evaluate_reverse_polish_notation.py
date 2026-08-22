import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op_function = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        for token in tokens:
            if token in op_function:
                y = stack.pop()
                x = stack.pop()
                stack.append(op_function[token](x, y))
            else:
                stack.append(int(token))

        return stack[0]
