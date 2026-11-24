# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        prev_value = None 
        while currentNode:
            save_link = currentNode.next
            currentNode.next = prev_value
            prev_value = currentNode
            currentNode = save_link
        return prev_value
        