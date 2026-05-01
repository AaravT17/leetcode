from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Approach 1
        # use a hashmap to store:
        # 1. each node against its index
        # 2. each index against the next index in the reordered list
        # indices = {}
        # curr = head
        # i = 0
        # while curr is not None:
        #     indices[i] = curr
        #     curr = curr.next
        #     i += 1

        # # at this point, i = # nodes in list
        # n = i

        # next_index = {}
        # for i in range((n - 1) // 2):
        #     next_index[i] = n - i - 1
        #     next_index[n - i - 1] = i + 1

        # if n % 2 == 0:
        #     next_index[(n - 1) // 2] = n // 2

        # last_item = None
        # for curr_i, next_i in next_index.items():
        #     indices[curr_i].next = indices[next_i]
        #     last_item = next_i  # need to set pointer of last "next" to None

        # if last_item is not None:
        #     indices[last_item].next = None
        # Time: O(n), Space: O(n)

        # Approach 2
        # Step 1: Find the second half of the linked list
        slow, fast = (
            head,
            head.next,
        )  # we are guaranteed to have at least one node in the list i.e. head is not None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        # second half starts at slow.next
        curr = slow.next
        slow.next = None  # split into two separate halves

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: Merge the two halves
        # end of second half (beginning once reversed) is at prev
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        # Time: O(n), Space: O(1)
