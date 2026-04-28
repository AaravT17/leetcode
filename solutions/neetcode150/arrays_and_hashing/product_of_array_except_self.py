from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        # Approach 1: Prefix and Suffix Products
        # n = len(nums)
        # prefix_product, postfix_product = [1] * n, [1] * n
        # for i in range(1, n):
        #     prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        #     postfix_product[n - i - 1] = postfix_product[n - i] * nums[n - i]
        # return [prefix_product[i] * postfix_product[i] for i in range(n)]
        # Time: O(n), Space: O(n)

        # Approach 2: Prefix and Suffix Products with O(1) Space
        n = len(nums)
        res = [1] * n
        # first pass -> store prefix product in res
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # second pass -> multiply prefix product with postfix product, use running variable to store postfix product
        postfix_product = 1
        for i in range(n - 2, -1, -1):
            postfix_product *= nums[i + 1]
            res[i] *= postfix_product

        return res
        # Time: O(n), Space: O(1)
