# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        def middleNode(node):
            mid=node
            fast_curr=node
            while fast_curr:
                if fast_curr.next is None:
                    return mid
                fast_curr=fast_curr.next.next
                mid=mid.next
            return mid
        def reverse(node):
            prev=None
            curr=node
            while curr is not None:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        temp=middleNode(head)
        mid=reverse(temp)
        curr=head
        curr_sum=0
        max_sum=0
        while curr!=mid and curr.next is not None:
            curr_sum=curr.val+mid.val
            if curr_sum>max_sum:
                max_sum=curr_sum
            curr=curr.next
            mid=mid.next
        return max_sum

        