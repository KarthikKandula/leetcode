# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Recursive solution
        the solution is very similar to iterative solution but just with recursive characteristics

    every node has two values
        val -- indicates current value
        next -- links to next value

    in the recursive function we take two pointers
        prev -- points to the previous node
        curr -- points to the current node

    in any function call, perform the following
        base condition -- check if curr node is none - if it is, return prev node
        assign next value (from curr node) to a temp node
        assign prev value to the next value in curr node -- essentially reversing the chain
        we're performing the below two functions as part of the recursive function call
            assign curr node to prev node -- helpful for ops in next iteration
            assign temp node (next node value) to curr node -- helpful for ops in next iteration

        in this loop we're 
            reversing the chain
            updating prev & curr pointers so they're helpful for the next loop
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define recursive function - two arguments curr & prev
        def traverse(curr, prev):
            # check if curr is none -- base condition for recursive function
            if not curr:
                return prev # return prev -- if curr is empty
            else: # means curr is not empty
                # temp variable to store next value
                nxt = curr.next
                # reverse the link by updating next to prev -- reversing is done for this node
                curr.next = prev
                # assign next node as current node & current node as prev  -- useful in next loop -- similar to iterative
                return traverse(nxt, curr) # recursive function call to traverse next node
        
        # return previous node -- since every current node becomes prev in above loop
        return traverse(head, None)

    """
    Iterative solution

    every node has two values
        val -- indicates current value
        next -- links to next value

    we take two pointers
        prev -- points to the previous node
        curr -- points to the current node

    loop as long as the curr node is valid
        assign next value to a temp node
        assign previous value to the next value in current node -- essentially reversing the chain
        assign current node to prev node -- helpful for ops in next iteration
        assign temp node (next node value) to curr node -- helpful for ops in next iteration

        in this loop we're 
            reversing the chain
            and updating prev & curr pointers so they're helpful for the next loop
    """
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # two pointers for iterative solution
    #     prev, curr = None, head
    #     # prev - to keep track of the previous node since reversing
    #     # curr - to keep track of the current node

    #     # loop while curr record is valid
    #     while curr:
    #         # temp variable to store next value
    #         nxt = curr.next
    #         # reverse the link by updating next to prev -- reversing is done for this node
    #         curr.next = prev
    #         # assign current node as prev -- useful in next loop
    #         prev = curr
    #         # assign next node as current node -- useful for next loop
    #         curr = nxt
        
    #     # return previous node -- since every current node becomes prev in above loop
    #     return prev