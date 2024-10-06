# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    use basic linked list traversal along with basic math to solve the problem

    if we remember how to add numbers in match, we add them in reverse order anyways
        here giving the linked list in reverse order is actually helping us

    create a variable to hold carry at each location - initially set to 0

    loop thru the list while any of the current list has a number or carry is not 0
        get the value at that location from each list
        add values at that location from each list & carry
        get the carry value from sum -- get multiple using //
        get the remainder from sum -- to insert into next node -- using %

        insert remainder into a newly created node & assign it to curr.next

        update all pointer for next iteration

    return dummy's next at the end
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node 
        dummy = ListNode()
        curr = dummy # create a temp variable curr & assign dummy node to it

        # variable to hold carry 
        carry = 0

        # loop while l1 or l2 is valid (to adopt for one value has more digits)
        while l1 or l2 or carry: # adding carry is for edge case if we need to add the carry value to end ex - 7+8 = 15
            # get value from l1 -- if l1 is not null else get 0
            val1 = l1.val if l1 else 0
            # get value from l2 -- if l2 is not null else get 0
            val2 = l2.val if l2 else 0

            # add values from two lists & carry 
            out = val1 + val2 + carry

            # calculate carry
            carry = out // 10 # get's the multiple (without decimals)

            # calculate value to insert into node
            val = out % 10 # get's the remainder

            # insert into next node -- creating the next node for traversal 
            curr.next = ListNode(val)

            # update curr to next node -- for next iteration
            curr = curr.next
            l1 = l1.next if l1 else None # update l1 to next node -- for next iteration
            l2 = l2.next if l2 else None # update l2 to next node -- for next iteration

        # return dummy's next node, that's where the original output node starts
        return dummy.next
