from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Approach 1
        # for i in range(len(s) // 2):
        #     s[i], s[-i - 1] = s[-i - 1], s[i]
        # This approach does not explicitly use two pointers, but it is
        # effectively doing so (L = i, R = -i - 1)

        # Approach 2:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
