class KthLargest:

    """
    we can solve this problem using heap
        maintain a heap of size k -- this will be a min heap
            i.e., values will be in ascending order
            so kth value will be in location 0

    create an array with input nums
    heapfiy this array

    check if heap has more than k values
        if it does, pop values from heap
    """
    def __init__(self, k: int, nums: List[int]):
        self.kth = k # variable to hold k value
        self.scores = nums # create array -- will be made to heap

        # heapify the array
        heapq.heapify(self.scores)

        # remove if there are more than k values in heap
        while len(self.scores) > self.kth:
            heapq.heappop(self.scores) # pop from heap

    """
    add input value to heap

    check if heap has more than k values
        if it does, pop values from heap
    
    return value in location 0 -- this is kth value
    """
    def add(self, val: int) -> int:
        # add new value to heap
        heapq.heappush(self.scores, val)

        # remove if there are more than k values in heap
        if len(self.scores) > self.kth:
            heapq.heappop(self.scores)  # pop from heap

        # return first value in heap -- since that's the kth value
        return self.scores[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)