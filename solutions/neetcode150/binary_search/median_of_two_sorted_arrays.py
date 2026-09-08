class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # let A be the shorter list
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        total = len(A) + len(B)
        half = total // 2  # = number of elements we need in left partition

        # let i mark the end of the left partition in A and j mark the end of the left partition in B
        # we need the left partition in B to have (half - number of elements in left partition in A) elements
        # j - 0 + 1 = half - (i - 0 + 1) => j = half - i - 2

        l, r = 0, len(A) - 1
        while True:
            i = l + ((r - l) // 2)
            j = half - i - 2
            # check if these partitions are correct i.e. they form the correct left partition for the combined list
            # for this to be the case, we need the last element in each <= next element after partition in the other
            # if not, grow/shrink left partition of A (and consequently do the opposite to left partition of B)
            last_left_A = A[i] if i >= 0 else float('-inf')
            next_A = A[i + 1] if (i + 1) < len(A) else float('inf')
            last_left_B = B[j] if j >= 0 else float('-inf')
            next_B = B[j + 1] if (j + 1) < len(B) else float('inf')

            if last_left_A <= next_B and last_left_B <= next_A:
                # partition is correct
                if total % 2 == 0:
                    # take avg of last element of left partition and first element of right partition (of combined list)
                    return (max(last_left_A, last_left_B) + min(next_A, next_B)) / 2
                else:
                    # take first element after left partition (of combined list)
                    return min(next_A, next_B)

            if last_left_A > next_B:
                # shrink the left partition in A (and grow the left partition in B)
                r = i - 1
            else:  # last_left_B > next_A
                # grow the left partition in A (and shrink the left partition in B)
                l = i + 1

        # no return statement needed after the while loop as a median must always exist
        # Time: O(log(min(m, n))) (binary search on shorter list) = O(log(m+n)), where m = len(nums1), n = len(nums2)
        # Space: O(1)
