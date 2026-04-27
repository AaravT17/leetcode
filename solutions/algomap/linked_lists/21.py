from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # if not list1:
        #     return list2
        # elif not list2:
        #     return list1

        # if list1.val <= list2.val:
        #     head = list1
        #     list1 = list1.next
        # else:
        #     head = list2
        #     list2 = list2.next

        # curr = head

        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         curr.next = list1
        #         curr = curr.next
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         curr = curr.next
        #         list2 = list2.next

        # if not list1:
        #     # that means we have added all elements of list1 to the joint list,
        #     # so we can proceed to add the remaining elements of list2 (we can
        #     # simply attach the remainder of list2 onto the joint list)
        #     curr.next = list2
        # else:
        #     # not curr2, i.e. we have added all elements of list2 to the joint
        #     # list, so we can proceed to add the remaining elements of list1
        #     # (we can simply attach the remainder of list1 onto the joint list)
        #     curr.next = list1

        # return head

        # Cleaner implementation using a dummy node
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if not list1:
            # that means we have added all elements of list1 to the joint list,
            # so we can proceed to add the remaining elements of list2 (we can
            # simply attach the remainder of list2 onto the joint list)
            curr.next = list2
        else:
            # not curr2, i.e. we have added all elements of list2 to the joint
            # list, so we can proceed to add the remaining elements of list1
            # (we can simply attach the remainder of list1 onto the joint list)
            curr.next = list1

        return dummy.next
