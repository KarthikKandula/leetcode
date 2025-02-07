# 962. Maximum Width Ramp

1 possible solution for this problem  


```
"""
    use monotonic stack (decreasing) and reverse order comparision to solve the problem
        the problem required to find the max value of j - i satisfying a condition
        a decreasing monotonic stack is best suited for this kind of problems
        first we populate the monotonic stack from start in decreasing order
        then loop from the end to compare value form the stack as well as value from end
            if satisfied the condition nums[i] <= nums[j]
            get the diff value & update a variable
        once all the values have been visited, we get the max possible value in result variable
"""
```

