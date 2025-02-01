# 3371. Identify the Largest Outlier in an Array

1 possible solution for this problem  


```
"""
    we can solve this problem using prefix sum
        the solution involves getting the sum of all values in nums
        we need to find the outlier
            the outlier can be found by 
                deducting any num from total -- diff
                if half value of this diff is in the array, it's a potential outlier
                but a condition exists, that the outlier should be different than current num
        
        so with this knowledge in mind we implement the below logic
            get prefix sum
            populate in a hashmap all values with their indexes
            for each num
                deduct this num from total -- diff
                half this diff
                check if this half is in hashmap
                    and that this half value isn't in the same index as current num
                if every condition is satisfied, update result value -- get max

        after going thru the array, max value is in result variable
"""
```

