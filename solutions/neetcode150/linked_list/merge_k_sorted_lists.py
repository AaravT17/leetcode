import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Approach 1
        dummy = ListNode()
        curr = dummy
        min_heap = []  # stores (value at head of list, idx of list)
        for idx, head in enumerate(lists):
            if head:
                min_heap.append((head.val, idx))
        heapq.heapify(min_heap)

        while min_heap:
            val, idx = heapq.heappop(min_heap)
            curr.next = lists[idx]
            curr = curr.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(min_heap, (lists[idx].val, idx))

        return dummy.next
        # Time: O(nlogk), Space: O(k), where n = num elements across all k lists

        # Approach 2
        # def merge_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        #     dummy = ListNode()
        #     curr = dummy
        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             curr.next = l1
        #             l1 = l1.next
        #         else:
        #             curr.next = l2
        #             l2 = l2.next
        #         curr = curr.next

        #     if l1:
        #         curr.next = l1
        #     else:
        #         curr.next = l2

        #     return dummy.next
        
        # if len(lists) == 0:
        #     return None
        
        # while len(lists) > 1:
        #     merged_lists = []
        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i+1] if i + 1 < len(lists) else None
        #         merged_lists.append(merge_lists(l1, l2))
        #     lists = merged_lists
        
        # return lists[0]
        # Time: O(nlogk), Space: O(k), where n = num elements across all k lists
