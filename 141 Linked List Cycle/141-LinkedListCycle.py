# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    use Floyd's Tortoise & Hare algorithm to solve the problem
        this uses two pointers - slow & fast
            slow -- moves 1 position with each iteration
            fast -- moves 2 positions with each iteration
        the algorithm says these two pointers will meet eventually if there is a cycle within n iterations
            time complexity is O(n)
    
    take two pointers -- slow & fast

    loop while fast & fast.next is valid
        move slow by 1 position
        move fast by 2 positions
        if slow & fast are equal return true

    in the end return false -- only hits if return is not hit within loop
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # take slow & fast pointer
        slow, fast = head, head

        # loop while fast & fast.next are valid
        while fast and fast.next:
            # if not fast.next:
            #     return False

            # move slow by one position
            slow = slow.next
            # move fast by two positions
            fast = fast.next.next

            # slow and fast are equal
            if slow == fast:
                return True # return true

        # return false if condition isn't hit in the loop
        return False

    """
    My solution
    """
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     hashmap = {}

    #     prev = None
    #     curr = head
    #     hashmap[curr] = None

    #     while curr:
    #         if curr.next in hashmap:
    #             return True
            
    #         hashmap[curr.next] = curr

    #         curr = curr.next
        
    #     return False