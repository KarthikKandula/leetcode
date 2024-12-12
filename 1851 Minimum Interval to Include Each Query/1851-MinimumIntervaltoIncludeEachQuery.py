class Solution:
    """
    the idea is to use a combination of data structures to solve the problem
        since the smallest interval is asked as part of the problem statement, it means we'd have to use a minHeap
        now, the operation's complexity occurs to knowing if a query is in the interval or not
            start & end values of the intervals are given
        instead of comparing for each query & for each interval -- very inefficient

        we break the comparisions & use them in combinations
        sort intervals by their starting values
        sort queries by their starting values

        take a pointer that keeps track of the current interval in processing -- i pointer

        now loop for each query
            insert all intervals the current query is in, into the minHeap
                use i pointer for the operation
                check i is in bounds & starting value of the interval is <= query value
                    if yes, insert into query in format - (diff (r-l+1), end value)
                    increment i count 
                if you notice, we're not inserting intervals into the heap for each query, just inserting them once
                    we don't have to reset the i counter cuz intervals are processed in sorted order
                    once an interval is added to the heap, it stays there as long as it applies to any future queries
            remove any elements in the minHeap that doesn't apply to the current query
                aka, the right/end value is less than current query value
                    since the value is end value of the interval, if it is less than current query
                    it means query value doesn't exist in that interval, remove it
                as long as the end value isn't less than any query, we don't remove it
                so we're inserting an interval once & reusing them as necessary for future queries
            get the lowest value from heap for the current query's smallest interval
                if a value exists, that the answer
                if the minHeap is empty, it means this query value doesn't exist in any interval
        
        in the end, return values from hashmap in a list format
    """
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals
        intervals.sort()

        # create hashmap to store values
        res = {}
        
        # create variable for counter
        i = 0

        # create minHeap
        minHeap = []

        # heapify minheap
        heapq.heapify(minHeap)

        # loop thru sorted queries list
        for q in sorted(queries):
            # insert values for any query into the heap
            # check i counter is within bounds & lowest value of the interval is <= current q val
            while i < len(intervals) and intervals[i][0] <= q:
                # extract left & right values
                l, r = intervals[i]
                # push into heap in format (diff, right)
                heapq.heappush(minHeap, (r - l + 1, r))

                # increment i pointer
                i += 1

            # remove unwanted values from the heap
            while minHeap and minHeap[0][1] < q:
                # pop from heap
                heapq.heappop(minHeap)

            # at this point, lowest values in the heap should be for this query
            # if not, this query isn't present in any of the intervals
            # insert lowest value into result hashmap
            res[q] = minHeap[0][0] if minHeap else -1

        # return a list of result
        return [res[q] for q in queries]
