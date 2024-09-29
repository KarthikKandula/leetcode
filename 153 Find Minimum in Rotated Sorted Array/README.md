# 153. Find Minimum in Rotated Sorted Array

1 possible solution for this problem  

## Method 1

To-do

### Self Notes
To achieve this we can use  binary search, it's basic implementation with a slight twist. as mentioned in the problem, the array is rotated, so a part of the array is sorted, there is a difference at a single point, which we need to find. use the formula left pointer value <= mid value, if it is left subarray is sorted, search in right subarray, if not, right subarray is sorted, search in left subarray. do this until condition is broken & you have the min value in result variable

```
"""
    Use binary search to solve the problem
        basic implementation of binary search with a slight twist

    as mentioned in the problem, the array is rotated, so a part of the array is sorted, there is a difference at a single point, which we need to find.
        use the formula left pointer value <= mid value
            if it is left subarray is sorted, search in right subarray
        if not
            right subarray is sorted, search in left subarray

    loop while left pointer <= right pointer
        calculate mid value
            replace if this is min value in result variable
        check if left pointer value <= mid value
            if it is left subarray is sorted, search in right subarray
        if not
            right subarray is sorted, search in left subarray

    loop thru end & answer is in result variable
"""
```
