# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    this is a basic linked list traversal problem with a couple twists
        to find if a string/number is palindrome we need to compare values from both sides
        in a linked list, going to end means we need to traverse the linked list
        best way to compare in efficient manner is
            get halfway point of the list
            reverse second half of the list
            compare each value from first half & second half of the list
                if a mismatch is found, return False
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # create slow & fast pointers to find mid point
        slow, fast = head, head

        # loop while fast & fast.next -- standard for finding mid point in ll
        while fast and fast.next:
            # move slow one place
            slow = slow.next
            # move fast two places
            fast = fast.next.next
        
        # if fast has a value -- it's an odd num list
        # in even num lists, fast is None
        if fast:
            # move slow one place since don't need to compare mid value
            slow = slow.next

        # reverse second list
        prev = None # to keep track of prev node
        cur = slow # keep track of cur node

        # loop while current node is valid
        while cur:
            nextNode = cur.next # get next node
            cur.next = prev # kill current node's link -- assign to prev
            
            prev = cur # assign cur node as prev -- for next iteration
            cur = nextNode # assign next node as cur -- for next iteration

        # now compare two lists
        second = prev # starting of second list
        first = head # starting of first list

        # loop as long as second is not none
        while second:
            # compare values
            if second.val != first.val:
                # return false if values don't match
                return False
            
            # if values match, move to next values
            second = second.next # move second list
            first = first.next # move first list

        # return True if false isn't triggered in loop
        return True
