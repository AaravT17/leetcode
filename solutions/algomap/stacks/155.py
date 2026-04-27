class MinStack:
    # Idea: 2 Stacks, on one stack, we push all elements, on the other,
    # we only push new minimums (or values equal to the current
    # minimum)
    def __init__(self):
        self.all_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.all_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        top_val = self.all_stack.pop()
        if self.min_stack and top_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.all_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
