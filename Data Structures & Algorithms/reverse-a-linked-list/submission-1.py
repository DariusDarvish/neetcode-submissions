# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dummy_node->0->1->2->3
        previous=None
        while(head):
            nxt=head.next
            head.next=previous
            previous=head
            head=nxt
        return previous
          
