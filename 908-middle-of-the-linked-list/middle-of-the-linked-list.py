# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        curr=head
        fast_curr=head
        while fast_curr:
            if fast_curr.next is None:
                return curr
            fast_curr=fast_curr.next.next
            curr=curr.next
        return curr
        