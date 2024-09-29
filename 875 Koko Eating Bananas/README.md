# 875. Koko Eating Bananas

1 possible solution for this problem  

## Method 1

To-do

### Self Notes
To achieve this we can use binary search in a creative way. The problem asks to find the lowest possible value that satisfies the condition. the trick here is to know the possible range of values first, and the range of values is from 1 to the max value in the input array piles. Since the range can be pretty high, we can consistently narrow down the range by implementing binary search. loop while left pointer is less than right pointer, find mid value & calculate the no. of hours taken to finish the piles using mid value, if it is <= h (hours gurads are away) we found a possible answer & replace the result variable with min value & decrement the right pointer since any future value is in the left subarray, vice versa, if the value is greater than h, we need to increment the left pointer since value might be in right subarray. do this until condition is broken & you have the min value in result variable

```
"""
    Use binary search to solve the problem
        the problem asks us to find the lowest possible value that satisfies a condition
        there are a range of values the answer can be in, to efficiently narrow down the possible values, we can use binary search

    take two pointers - left & right, on opposite ends of the range of possible values
        possible values are from 1....max(piles)
            anything less than 1 doesn't make sense & anything more than piles would be too fast
        
    loop while left pointer <= right pointer (since l & r can be at the same value & that can be the answer)
        calculate mid point for this iteration
        calculate hours taken to finish the pile
        if hours <= h (hours guards are away)
            it satisfies the condition, could be a possible answer
            decrement the right pointer since any other possible values are in the left subarray
        else
            it means it's going to take more speed to finish all the piles
            increment the left pointer, since any possible values are in right subarray
    
    loop thru end & answer is in result variable
"""
```
