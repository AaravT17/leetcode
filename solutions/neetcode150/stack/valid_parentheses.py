class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':  # opening parenthesis
                stack.append(c)
            else:  # closing parenthesis
                if not stack:
                    return False
                opening = stack.pop()
                if (c == ')' and opening != '(') or (c == '}' and opening != '{') or (c == ']' and opening != '['):
                    return False

        return True if not stack else False
