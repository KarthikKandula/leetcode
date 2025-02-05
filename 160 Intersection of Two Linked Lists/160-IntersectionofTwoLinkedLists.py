# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    the basic idea is to apply linked list traversal in creative ways
        to get the intersecting node without using any extra space
        we need to get the distance of each list to the end
        start from the same location from the end
            move each lists one node at a time
            if they meet, they'll meet at the same node at some point
            this node is the intersecting point
            
            if they don't meet, any of the list is going to become null
            hence we know the two lists never meet
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # function to get the distance to end
        def getDist(node):
            end = 0 # variable to store dist to end

            # loop while node is valid
            while node:
                node = node.next # move to next node
                end += 1 # increment node value
            
            return end # return dist value
        
        # get dist to end for A list
        cur = headA
        aDist = getDist(cur)

        # get dist to end for b list
        cur = headB
        bDist = getDist(cur)

        # adjust to same dist
        curA, curB = headA, headB
        # move up in A list to be at same dist from end
        for i in range(aDist - bDist):
            curA = curA.next
        # move up in B list to be at same dist from end
        for i in range(bDist - aDist):
            curB = curB.next

        # move both list one node at a time
        while curA and curB:
            # if both nodes are same, return that node 
            if curA == curB:
                return curA # return that node
            
            # move both nodes to next node
            curA = curA.next
            curB = curB.next
        
        # if return isn't triggered above, they don't meet
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        path = set()

        cur = headA

        while cur:
            path.add(cur)
            cur = cur.next

        cur = headB

        while cur:
            if cur in path:
                break

            cur = cur.next

        return cur if cur else None
