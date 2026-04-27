from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product, right_product = [1] * n, [1] * n
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
            right_product[n - i - 1] = right_product[n - i] * nums[n - i]
        return [left_product[i] * right_product[i] for i in range(n)]
