class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if char == ')':
                    if not stack or stack.pop() != '(':
                        return False
                elif char == '}':
                    if not stack or stack.pop() != '{':
                        return False
                else:  # char == ']'
                    if not stack or stack.pop() != '[':
                        return False

        return not stack
