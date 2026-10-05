class ListNode:
    def __init__(self,val,next_node=None):
        self.val=val
        self.next=next_node

class MyLinkedList:

    def __init__(self):
        self.head=ListNode(-1)

    def get(self, index: int) -> int:
        curr=self.head.next
        i=0
        while curr:
            if i==index:
                return curr.val
            i+=1
            curr=curr.next
        return -1
        
    def addAtHead(self, val: int) -> None:
        new_node=ListNode(val,self.head.next)
        self.head.next=new_node

    def addAtTail(self, val: int) -> None:
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=ListNode(val)
    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        curr=self.head
        while i<index and curr:
            i+=1
            curr=curr.next
        if curr:
            new_node=ListNode(val,curr.next)
            curr.next=new_node
        return

    def deleteAtIndex(self, index: int) -> None:
        i=0
        curr=self.head
        while i<index and curr:
            i+=1
            curr=curr.next
        if curr and curr.next:
            curr.next=curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)