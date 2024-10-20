class Solution:
    """
    solve this problem using heap
        python has minheap implementation -- for this problem we want the max heap
        to handle this, we'll negate all values -- so it'll implement maxheap
    
    insert values into an array by negating the values & heapify it

    loop while length of heap > 1
        pop two values from heap
        insert their difference if values are not equal
    by the end of this loop, heap either has 1 value or 0

    return value from heap if heap has value else return 0
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        # insert values from stones into a new array -- negative them to simulate max heap
        vals = [-x for x in stones]
        
        # heapify above array
        heapq.heapify(vals)

        # loop while length of heap is greater than 1 -- we need 1 or 0
        while len(vals) > 1:
            val1 = heapq.heappop(vals) # pop first value
            val2 = heapq.heappop(vals) # pop second value

            # check if values are not equal
            if not val1 == val2:
                # push into heap the difference of two values -- abs here to handle one value greater than the other
                heapq.heappush(vals, -abs(val1 - val2)) # insert -ve of the value

        # by this point heap either has 1 value or no values
        # return value from heap if it has a value -- abs it since all values are -ve
        return abs(vals[0]) if vals else 0 # else return 0, as per requirements
