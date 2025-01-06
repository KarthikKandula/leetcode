# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Approach 2

    This approach also involves dummy & cur node's
        at any time keep track of 3 nodes, prev, cur & cur.next
        in this approach, we're doing operations from the stand point of the curr node

        taking backup of the first node in next iteration is an additional step
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if input is empty ll, return empty ll
        if not head:
            return head
        
        # create dummy node
        dummy = ListNode(0)
        dummy.next = head # point dummy node to head -- give constant starting point

        # create 2 new pointers, prev & curr to point at nodes
        prev, cur = dummy, head

        # loop while cur & cur.next are valid
        while cur and cur.next:
            # take backup of the first node in next iteration, to point correctly
            bckup = cur.next.next
            
            # get second node, next to curr node
            second = cur.next
            
            # perform swapping ops
            second.next = cur # relink second node to current node
            cur.next = bckup # relink current node to backup node i.e., 1st node in next iteration
            prev.next = second # relink prev node to second node, since appears first now

            # reassign pointers to help in next iteration
            prev = cur
            cur = bckup
        
        # return dummy.next node, always points to head
        return dummy.next

    """
    Approach 1

    This approach involves dummy & cur node's
        at any time keep track of 3 nodes, cur, cur.next & cur.next.next
        in this approach, we're doing operations from the stand point of the before/prev node
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next

            cur.next = second
            first.next = second.next
            second.next = first

            cur = first

        return dummy.next


