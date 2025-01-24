# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    this is a classic linkedlist traversal problem
        we can solve this problem using two pointers for odd & even nodes
        kill & reestablish links between odd nodes
        kill & reestablish links between even nodes
        in the end create link from odd's end to even's start
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is empty
        if not head:
            # return null
            return None
        
        # odd & even pointers
        odd, even = head, head.next
        evenHead = head.next # pointer to point at even's head

        # loop while even & even's next are valid -- stops when even reaches last node
        while even and even.next:
            # reassign curr odd's next pointer to the next odd node
            odd.next = odd.next.next
            odd = odd.next # reassign odd node for next iteration

            # reassign curr even's next pointer to the next even node
            even.next = even.next.next
            even = even.next # reassign even node for next iteration
        
        # at this point have two diff lists, odd & even list
        # create link between odd's end to even's head
        odd.next = evenHead

        # return head of newly updated node
        return head

