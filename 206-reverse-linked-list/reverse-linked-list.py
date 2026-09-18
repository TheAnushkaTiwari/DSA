# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        curr=head
        while curr is not None:
            next_node=curr.next #save the next node
            curr.next=prev      #reverse the link
            prev=curr           #move previous one step forward
            curr=next_node      #move curr one step forward
        return prev
        