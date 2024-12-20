# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    this is a classic slow & fast pointer problem
        move the pointers in below method
            move slow pointer by one hop
            move fast pointer by two hops
        loop while fast & fast.next isn't none
        once the loop ends, the slow pointer is pointing at the mid of linked list
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create slow & fast pointers at head of the linked list
        slow, fast = head, head

        # loop while fast & fast.next isn't none
        while fast is not None and fast.next is not None:
            slow = slow.next # move slow pointer by one hop
            fast = fast.next.next # move fast pointer by two hops
        
        # return slow pointer
        return slow
