from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]  # +1 because the problem is 1-indexed
            elif total < target:  # increase sum by moving l right
                l += 1
            else:  # decrease sum by moving r left
                r -= 1
        # don't need a return statement outside the loop, the problem guarantees that there is always a solution
        # Time: O(n), Space: O(1)
