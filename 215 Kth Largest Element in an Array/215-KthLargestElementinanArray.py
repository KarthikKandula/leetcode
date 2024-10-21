class Solution:
    """
    Alternate efficient coded solution

    use heap to solve the problem
        we'll implement a heap with length k
        insert k elements from input into heap
        for every other element in nums, check if it is greater than lowest element in heap
            if it is, replace that element by popping & pushing into heap
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k] # create an array & get k elements from input nums
        heapq.heapify(heap) # heapify above array

        # loop nums array starting from kth element
        for n in nums[k:]:
            # check if current num is greater than lowest element in heap
            if n > heap[0]:
                # if it is, replace that value in heap
                heapq.heappop(heap) # pop lowest value from heap
                heapq.heappush(heap, n) # push this value to heap
        
        # return first location value -- since this is a minheap of length k
        return heap[0]

    """
    My solution

    create a new array same as input nums
    heapify this new array
    run a loop for the length of (length of heap - k) + 1
        continously pop from heap
    
    last popped value is the kth largest element
    """
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # create new array for nums
    #     vals = nums

    #     # heapify vals 
    #     heapq.heapify(vals)

    #     # get length of vals
    #     lenVals = len(vals)

    #     # loop until we get to the kth larget element -- using formula (length of vals - k) + 1
    #     for i in range((lenVals - k) + 1):
    #         val = heapq.heappop(vals) # popo from heap & save it to a variable

    #     # return last popped variable -- that is the kth element
    #     return val