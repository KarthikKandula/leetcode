class Solution:
    """
    this is a classic interval problem as well as dynamic programming
        there are seperate arrays for start time, end time & profit
        since we need to find max profit without overlapping intervals
        we need to combine the values & sort them by start time
            gives a list we can work with
        now, this becomes a backtracking problem to find the max profit
            two possibilities exist
                skip current interval
                include current interval
                    if you include current interval
                    need to make sure to call next interval that isn't overlapping
            return the max of skipped value & included value
    """
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # create new list of tuples with combined start & end times
        # sort the array based on start times
        intervals = sorted(zip(startTime, endTime, profit))

        # create cache to avoid repeated calls
        cache = [-1] * len(intervals)

        # recursive function to implement dp
        def dfs(i):
            # base conditions
            # if i reaches end
            if i == len(intervals):
                return 0
            # if this index has already been visited
            if cache[i] != -1:
                return cache[i] # return from cache
            
            # two possible options
            # skip current position
            skip = dfs(i + 1)


            # include current position -- if this is the case, need to find unconflicting interval
            # j = i + 1
            # while j < len(intervals):
            #     if intervals[i][1] <= intervals[j][0]:
            #         break
                
            #     j += 1
            
            # use binary search to find next interval not conflicting with current
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))

            # recursive call for that index
            include = dfs(j)

            # get the max value of skipped ops & include ops 
            cache[i] = max(skip, intervals[i][2] + include)

            # return value to calling function
            return cache[i]

        # initial call for recursive function
        return dfs(0)
