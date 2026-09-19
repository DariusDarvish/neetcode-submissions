# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left=0
        node_array=[]
        dummy = node = ListNode()
        while(head):
            node_array.append(head)
            head=head.next
        right=len(node_array)-1
        while(left<right):
            node.next=node_array[left]
            node=node.next
            left+=1
            print(node.val)
            node.next=node_array[right]
            node=node.next
            right-=1
            print(node.val)
            if(left==right):
                node.next=node_array[left]
                node=node.next
                print(node.val)
            node.next=None
        

        



