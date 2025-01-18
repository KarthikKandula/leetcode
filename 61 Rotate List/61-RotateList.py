# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    we can solve this using basic linked list traversal
        to rotate the list by k places
            we need the last node
            and length of the list
        use a pointer to traverse thru the list
            to point at last node
            also to get the length of list

        if we have to rotate the list by k places
            we need to get the node at length - k - 1 location
            the next node at this position is going to be the new head node
        loop thru the input again, to get to new head node
            kill connection with next node
            establish connection with last node to head node
    
    return new head node in the end
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base condition -- handle empty lists
        if not head:
            return head
        
        # to find lst node & count
        last, count = head, 1

        # loop thru each node to get count & last pointer pointing at last node
        while last.next:
            last = last.next
            count += 1

        # new pointer facing at start
        cur = head

        # get modified k value -- to handle k > length of list
        k = k % count

        # if no rotations need to be made
        if k == 0:
            return head

        # loop for count - k - 1 jumps to get to new head
        for i in range(count - k - 1):
            cur = cur.next

        # get new head value -- pointing at cur.next
        newHead = cur.next

        # kill link of last node in modified list
        cur.next = None

        # point last node to head 
        last.next = head

        # return newHead node
        return newHead
