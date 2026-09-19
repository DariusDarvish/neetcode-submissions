# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index_dict={}
        while(head):
            if head not in index_dict:
                index_dict[head]=True
            else:
                return True
            head=head.next
        return False
