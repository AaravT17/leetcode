# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # maintain a gap of n+1 between slow and fast ptrs (n+1 rather than n since we wanna remove the nth node 
        # from the end so we need to be at the (n+1)th from the end to jump so we can jump over the nth)
        dummy = ListNode(next=head)
        slow = fast = dummy
        i = 0
        while i < n + 1:
            fast = fast.next
            i += 1
        
        while fast:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        return dummy.next
