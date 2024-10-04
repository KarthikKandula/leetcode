# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Neetcode influenced own solution

    the objective is to remove nth node from the last
        the way we can go to this location at once is if we use two pointers
            left - starts at head
            right - initially starts n places from left
                at this point we handle a edge case where the first node has to be removed
        after that we advance left & right equally until right reaches end
    
    at this point left points to the before node of the one that has to be removed
        kill the link to the node that has to be removed & create link to the node after that
    
    return head at the end
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create left & right pointers at head
        left, right = head, head

        # advance right pointer by the length of n
        for k in range(n):
            right = right.next # advance right pointer

        # if right pointer is None, we can return head.next -- to handle edge case where we remove first node
        if not right: # if right is empty
            return head.next

        # loop while right.next is not none
        while right.next:
            left = left.next # advance left pointer
            right = right.next # advance right pointer

        # now left pointer stops just before the node that has to be removed
        left.next = left.next.next # remove the link to next node & assign to node after that

        # return head 
        return head

    """
    My solution
    """
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # hashmap = {} # create hashmap to get locations of each node

        # # create temp node to take copy of head
        # temp = head
        # i = 1 # variable to get count

        # # loop while temp is not none
        # while temp:
        #     hashmap[i] = temp.val # add location & value to hashmap
        #     temp = temp.next # keep temp node moving
        #     i += 1 # increment count variable

        # # calculate target value that has to be removed
        # target = (len(hashmap) - n) + 1

        # # create two pointers prev & curr
        # prev, curr = None, head
        # j = 1 # variable to keep count 

        # # loop while curr is not none
        # while curr:
        #     # check if current value is same as target value & the count matches
        #     if curr.val == hashmap[target] and target == j:
        #         # this is to handle an edge case where removing first node
        #         if not prev: # if prev is None
        #             head = curr.next # assign head to curr's next value
        #             break # break loop

        #         # if prev is not none
        #         prev.next = curr.next # assign prev's next value to curr's next value -- essentially killing the current node's link
        #         curr.next = None # remove curr node's link to any other nodes
        #         break # break loop
        #     else: # if curr node is not the right node
        #         tmp = curr # create a temp node to hold curr value
        #         prev = curr # assign curr value to prev node
        #         curr = tmp.next # assign next node's value to curr

        #         j += 1 # increment count value

        # # return head
        # return head