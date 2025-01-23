# 1235. Maximum Profit in Job Scheduling

1 possible solution for this problem  


```
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
```

