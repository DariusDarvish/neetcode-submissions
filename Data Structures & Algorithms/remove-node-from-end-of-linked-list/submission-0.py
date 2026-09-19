# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current_slow_node=head
        current_fast_node=head
        previous_node=None
        for x in range(n):
            current_fast_node=current_fast_node.next
        while(current_fast_node != None):
            previous_node=current_slow_node
            current_slow_node=current_slow_node.next
            current_fast_node=current_fast_node.next
        if previous_node:
            previous_node.next=current_slow_node.next
        else:
            head = head.next 
        return head

        


            
