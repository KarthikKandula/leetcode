# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    we can use basic linked list manipulation techniques to solve the problem
        if we can find the second half of the list & manage to reverse it
        at the end it's just joining both the lists

    the problem can be divided into two parts
        need to divide the list into two subarrays
            first - has the first half of the list (bigger if odd)
            second - has the second half of the list
    
    now we reverse second subarray of the list

    after reversing, manipulate the nodes in such a way that they're placed in the asked format
        might have to use multiple temporary nodes
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid point of the list 
        # create slow & fast pointers to get to mid point -- slow gets to mid point
        slow, fast = head, head.next
        # loop while fast & fast.next are not null
        while fast and fast.next:
            slow = slow.next # slow goes by 1 hop
            fast = fast.next.next # fast goes by 2 hops

        # reverse second subarray
        # at this point slow is at the end of the first subarray
        second = slow.next # assign the start of second subarray to second 
        slow.next = None # assign slow.next to None since it's going to the end of the new array
        prev = None # previous pointer for reversing 
        # here second is same as curr

        # loop while second is valid
        while second:
            nxt = second.next # temp variable to store next node
            second.next = prev # reverse the link to prev node
            prev = second # assign curr node as prev node
            second = nxt # assign next node (in tmp nxt variable) as curr node (second here)

        # update list in place acc to ask
        first = head # this is the start of first subarray
        second = prev # this is the start of second subarray

        # loop while first & second nodes are valid
        while first and second:
            # two temp nodes to hold the next value of first & second
            tmp1, tmp2 = first.next, second.next

            # temp value to hold first's next value
            nxt = first.next
            first.next = second # update first node's next value to second 
            second.next = nxt # update second node's next value to temp nxt value

            first = tmp1 # update first node to temp node -- for next iterations
            second = tmp2 # update second node to temp node -- for next iterations

        