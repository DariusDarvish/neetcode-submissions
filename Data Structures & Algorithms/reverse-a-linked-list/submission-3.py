# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous=None
        current=head
        while current:
            #1
            nxt=current.next
            current.next=previous
            #None<-0
            previous=current

            current=nxt
           
            

        return previous
            