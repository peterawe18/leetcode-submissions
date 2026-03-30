# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        previous_node = None

        # T O(n) M O(1)
        while(current_node != None):
            nxt = current_node.next

            current_node.next = previous_node

            previous_node = current_node

            current_node = nxt

        return previous_node
