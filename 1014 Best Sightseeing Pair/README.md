# 1014 Best Sightseeing Pair

1 possible solution for this problem  

## Method 1

### Self Notes


```
"""
   we can solve this using dynamic programming
      the prob desc asks to calculate max value for values[i] + values[j] + i - j where i < j
      we can dissect the formula into the max of values[i] + i + values[j] - j
      we keep track of max values[i] + i in a variable
      calculate values[j] - j for each position & update maxScore accordingly
         one more thing is to only update values[i] + i after values[j] - j along with maxScore is calculated for curr position
         to satisfy condition i < j
"""
```
