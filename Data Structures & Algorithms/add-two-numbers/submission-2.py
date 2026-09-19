# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode()
        node=dummy_node
        carry=0
        while(l1 or l2):
            l1_val=l1.val if l1 else 0
            l2_val=l2.val if l2 else 0
            new_val=l1_val+l2_val+carry
            carry=0
            if(new_val<10):
                node.next=ListNode(new_val)
            else:
                carry=new_val // 10
                module_new_val= new_val % 10
                node.next=ListNode(module_new_val)  
            node=node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
           
        if(carry>0):
            node.next=ListNode(carry)
        return dummy_node.next
        