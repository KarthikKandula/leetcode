class Solution:
    """
    solve this problem using minHeap & set
        minHeap is useful to always get the lowest value from the remaining values
        the idea is to use the set to record marked indexes

    insert all values in nums to the heap in format -- [value, index]

    loop while minHeap has values
        get rid of all the values in minHeap whose indexes are already in set
            after this operation, the lowest value in heap is unmarked
        
        get the lowest value from heap
            add value to score variable
            add it's index along with adjacent indexes to set

    in the end return score value
    """
    def findScore(self, nums: List[int]) -> int:
        # create minHeap
        minHeap = []

        # loop thru input nums to insert values into minHeap
        for i, v in enumerate(nums):
            minHeap.append([v, i])
        
        # heapfiy minHeap
        heapq.heapify(minHeap)

        # create set to track marked values
        marked = set()
        score = 0 # variable to record output score

        # loop while minHeap has values & marked set doesn't have all values
        while minHeap and len(marked) != len(nums):
            # remove any unnecessary elements from minHeap
            # remove all values from heap if the index is already in minHeap
            while minHeap and minHeap[0][1] in marked:
                heapq.heappop(minHeap) # pop from the index

            # get lowest element
            lowVal, lowInd = heapq.heappop(minHeap)

            # add to score
            score += lowVal

            # add to set, two adjacent elements
            marked.add(lowInd)
            if lowInd - 1 >= 0:
                marked.add(lowInd - 1)
            if lowInd + 1 < len(nums):
                marked.add(lowInd + 1)
        
        # return score value
        return score
