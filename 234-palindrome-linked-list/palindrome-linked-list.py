# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        def middle(node):
            curr=node
            fast_curr=node
            while fast_curr:
                if fast_curr.next is None:
                    return curr
                fast_curr=fast_curr.next.next
                curr=curr.next
            return curr
        mid=middle(head)
        def reverse(node):
            prev=None
            curr=node
            while curr is not None:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        reversed_list= reverse(mid)
        curr=head
        while reversed_list:
            if curr.val!=reversed_list.val:
                return False
            curr=curr.next
            reversed_list=reversed_list.next
        return True
        