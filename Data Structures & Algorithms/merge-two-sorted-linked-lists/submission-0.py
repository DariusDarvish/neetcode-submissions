# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        while(list1 and list2):
            if(list1.val< list2.val):
                next_node=list1.next
                head.next=list1
                list1=next_node
            else:
                next_node=list2.next
                head.next=list2
                list2=next_node
            
            head=head.next
        if(list1==None):
                head.next=list2
        elif(list2==None):
                head.next=list1
        return dummy.next
                