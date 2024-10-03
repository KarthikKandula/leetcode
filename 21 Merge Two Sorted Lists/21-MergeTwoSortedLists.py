# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    the solution uses classic linked list traversal technique to sort the two lists
        the additional part here being creating a dummy node to get things started. 

    create a temp node called tail that will be the running node where things will be added to. 

    loop while both lists are valid
        check for the lowest value and add it to the list first
            adding to the list means, adding it to tail
            after adding make sure to update the respective list's node to the next value
        in every loop, make sure to update tail to become the last node -- useful for next iterations
    
    it is possible some lists are longer than others so the previous loop ends without going thru everything
        check if anything is left in the lists
            if there is, assign remaining of the list to tail
    
    in the end return dummy's next value -- that's where the new list starts
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create an empty node to start ops
        dummy = ListNode()
        tail = dummy # create a tail node -- that indicates the start of the new sorted list

        # loop while both lists are not null
        while list1 and list2:
            # check if list1.val < list2.val
            if list1.val < list2.val:
                tail.next = list1 # assign the node to tail's next value -- since tail always is the last node in list
                list1 = list1.next # update list1 to be next value in it's list
            else:
                tail.next = list2 # assign the node to tail's next value -- since tail always is the last node in list
                list2 = list2.next # update list2 to be next value in it's list

            # updating tail to the latest/last node in the list -- to help with future iterations
            tail = tail.next

        # check if there are any left out nodes in list1
        if list1:
            # if there are, assign the rest of list1 to tail
            tail.next = list1
        # check if there are any left out nodes in list2
        elif list2:
            # if there are, assign the rest of list2 to tail
            tail.next = list2

        # return dummy's next value, that's where the list begins
        return dummy.next

