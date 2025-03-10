# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    we can solve this using basic linked list reversal techniques with a bit of twists
        we need to locate the left node
        once hit the left node, need to reverse each node from then on
        once hit the right node, need to stop the reversing process
            and make final links
        using a dummy node is going to help since makes it easy if left == 1
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if input is empty or left & right are the same nodes, no reversing
        if not head or left == right:
            return head # return head 

        # create dummy node for easy operations
        dummy = ListNode(0)
        dummy.next = head # create link between dummy & head

        # create sample nodes for before start & start nodes
        beforStart, start = None, None

        # create prev & cur nodes
        prev, cur = dummy, head
        count = 0 # make count = 0

        # loop while count is less than right
        while count < right:
            # get next node -- backup
            nxt = cur.next
            count += 1 # increment count for this node

            # if hit left, take backup
            if count == left:
                # backup the node before start reversing
                beforStart = prev
                start = cur # record the starting node in reversing nodes
                prev.next = None # remove link to the previous node -- will be connected later
            
            # if count is greater than left, need to reverse this node
            if count > left:
                # assign current's next to prev -- reversing
                cur.next = prev
            
            # if count is at right -- end reversing
            if count == right:
                # assign the node before starting reversing to current node
                beforStart.next = cur
                # create link with the first node in reversing to the next node -- completing the ll
                start.next = nxt

            # move pointers, for next iterations
            prev = cur
            cur = nxt

        # return dummy's next node -- the starting of linked list
        return dummy.next
