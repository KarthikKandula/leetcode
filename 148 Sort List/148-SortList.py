# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    using MergeSort

    the basic idea of the problem is to apply merge sort to the linked list
        merge sort involves breaking the input into two equal parts
            until we have individual nodes
            at this point we can start combining nodes in a sorted manner
                use two pointer comparision technique
            keep doing this until the entire list is formed
        
        the only twist here being to find the mid point in every linked list
            we need to start fast pointer at fast.next -- just to reach the right mid point
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if input doesn't have head or only a single node
        if not head or not head.next:
            return head # return that node

        # split into two lists
        # call helper function to get the start of second list
        left, right = head, self.getMid(head)

        # kill the link between first & second lists
        rightNext = right.next # get right's next node -- starting point of right list
        right.next = None # kill link for left's last node
        right = rightNext # reassign right to it's new start node

        # recursive calls to split 
        left = self.sortList(left)
        right = self.sortList(right)

        # merge lists together
        # return merged list
        return self.mergeLists(left, right)

    def mergeLists(self, left, right):
        # two pointers pointing at start nodes in each list
        first, second = left, right

        # create dummy node -- start node for new list
        dummy = ListNode()
        temp = dummy # create temp node from dummy -- doing all ops

        # loop while first & second hav valid nodes
        while first and second:
            # compare pointers
            # get lower one first
            if first.val <= second.val:
                temp.next = first
                first = first.next
            else:
                temp.next = second
                second = second.next
            
            temp = temp.next

        # if anything left of the first list
        if first:
            temp.next = first

        # if anything left of the second list
        if second:
            temp.next = second

        # return combined list
        return dummy.next

    # recursive function to get mid point of each list
    def getMid(self, head): 
        # classic slow, fast pointer
        # starting fast from head.next to get the right mid point
        # if fast is at head, leads to uneven mid points in even length lists
        slow, fast = head, head.next

        # loop while fast & fast.next are valid
        while fast and fast.next:
            slow = slow.next # skip slow one node
            fast = fast.next.next # skip fast two nodes
        
        # return slow node
        return slow

    """
    using Heap
    """
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    #     heap = []

    #     heapq.heapify(heap)

    #     curr = head

    #     while curr:
    #         heapq.heappush(heap, curr.val)
    #         curr = curr.next
        
    #     cur = head

    #     while cur:
    #         popVal = heapq.heappop(heap)
    #         cur.val = popVal

    #         cur = cur.next
        
    #     return head
