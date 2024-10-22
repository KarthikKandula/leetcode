class MedianFinder:
    """
    to solve this problem we have to continously sort input nums are we receive
        sorting a single heap continously & accesing values to calc median is too much work
    to get around this problem
        create two heaps -- small & large
            smallHeap is a maxHeap
            largeHeap is a minHeap
            values in smallHeap will always be less than values in largeHeap
            their length will only ever differ by 1 unit
    """
    def __init__(self):
        self.smallHeap = [] # maxHeap implementation
        self.largeHeap = [] # minHeap implementation

        # heapify arrays
        heapq.heapify(self.smallHeap)
        heapq.heapify(self.largeHeap)

    """
    add any input value to the smallHeap

    check if values in heaps are in order
        if smallHeap's max value is greater than largeHeap's min value -- swap them around
            pop from smallHeap
            insert into largeHeap
    
    check if heaps are balanced
        if length of any heaps is greater than 2 of other
            swap values around 
    """
    def addNum(self, num: int) -> None:
        # insert into small heap
        heapq.heappush(self.smallHeap, -1 * num) # negate to simulate maxHeap

        # check if values are in order
        # if both heaps have values & smallHeap's highest value is greater than largeHeap's min value
        if self.smallHeap and self.largeHeap and ((-1 * self.smallHeap[0]) > self.largeHeap[0]):
            # pop from smallHeap
            tempVal = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, tempVal) # insert into largeHeap
        
        # check if heaps are imbalanced
        # check if smallHeap is longer than largeHeap
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            # pop from smallHeap
            tempVal = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, tempVal) # insert into largeHeap
        # check if largeHeap is longer than smallHeap
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            # pop from smallHeap
            tempVal = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * tempVal) # insert into largeHeap

    """
    check if length of any heap is greater than other
        odd no. of values -- return value from greater heap
    if length is same
        return calculation -- smallHeap's max value + largeHeap's min value / 2
    """
    def findMedian(self) -> float:
        # check if heaps are not equal
        # if smallHeap has more values than largeHeap -- total nums are odd
        if len(self.smallHeap) > len(self.largeHeap):
            return -1 * self.smallHeap[0] # return smallHeap's max value
        # if largeHeap has more values than smallHeap -- total nums are odd
        elif len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0] # return largeHeap's min value
        # both heaps have same no. of values -- total nums are even
        else:
            # calculate median value
            return ((-1 * self.smallHeap[0]) + self.largeHeap[0]) / 2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()