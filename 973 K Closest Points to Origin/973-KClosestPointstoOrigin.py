class Solution:
    """
    solve this problem using heap -- python has minheap, that is perfect for the solution

    calculate distance for each point & store it in an array in format - [dist, x, y]

    heapify the array

    loop for k times
        pop from heap
        append x & y coordinates to result array

    return result array 
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create result array
        res = []
        # create array to store sqrt, x, y values
        minHeap = []

        # calculate distance for each point
        for x, y in points:
            tempDist = x**2 + y**2 # calc distance for current point -- no need sqrt
            minHeap.append([tempDist, x, y]) # append to array in format [dist, x, y]

        # heapify the array
        heapq.heapify(minHeap)

        # loop for k times -- to extract k items from heap -- since minheap will get lowest k values
        for i in range(k):
            # pop from heap & store in variables
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y]) # append to result array

        # return result array
        return res
