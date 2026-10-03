# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=fast_curr=head
        while fast_curr and fast_curr.next:
            curr=curr.next
            fast_curr=fast_curr.next.next
            if fast_curr==curr:
                ptr=head
                while ptr!=curr:
                    ptr=ptr.next
                    curr=curr.next
                return ptr
        return None
        