class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i: int) -> None:
            if i == n:
                res.append(sol[:])  # append a COPY of the solution to the result
                return

            # path 1: do not include nums[i] in the solution
            backtrack(i + 1)

            # path 2: include nums[i] in the solution
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            # when we return to this level in the recursion tree, nums[i] appended to the solution at this level
            # is the last remaining element since elements appended in subsequent recursive calls are popped off
            # before returning to the previous level

        backtrack(0)
        return res
        # Time: O(2^n)
        # Space: O(n)
