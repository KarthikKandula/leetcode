# 167. Two Sum II - Input Array Is Sorted

1 possible solutions for this problem

## Method 1

The problem statement specifies to look for two numbers (indexes) from an array that add up to a target number. And since the input is already sorted, we can condifently use two pointers & increment any of the pointers based on the sum of the values at a location.  

```
"""
    Use two pointers, one at start, one at end
        
    compare the sum of start & end 
        if greater than target -> decrease end
        if less than target -> increase start
        if match found -> return indexes
"""
```
