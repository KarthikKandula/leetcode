# 33. Search in Rotated Sorted Array

1 possible solution for this problem  

## Method 1

We can solve this problem using **binary search** with a slight modification to handle the rotated sorted array.

1. **Binary search with rotation**:
   - Normally, binary search works on a fully sorted array, but in this case, the array is rotated. The key is to determine which side (left or right) of the array is sorted during each iteration of the binary search.
2. **Check if left or right subarray is sorted**:
   - For each iteration, check if the **left half** of the array (from `low` to `mid`) is sorted:
     - If the left subarray is sorted, check if the target lies within this range. If it does, perform binary search on the left subarray.
     - If the target does not lie in the sorted left subarray, move the search to the **right subarray**.
   - If the left subarray isn't sorted, then the **right half** must be sorted:
     - Check if the target lies in the right subarray. If it does, search in the right subarray.
     - If it doesn't, move the search back to the left subarray.
3. **Repeat until target is found**:
   - Continue narrowing down the search space based on which subarray is sorted until the target is found or the search space is exhausted.

This approach leverages binary search to maintain efficiency while handling the rotated aspect of the array.

### Self Notes
To achieve this we can use  binary search, it's basic implementation with a slight twist. as mentioned in the problem, the array is rotated & we need to find an element in this array, the key is to check if the left & right subarrays are sorted & if the target is in there, if it is we search in that particular subarray, if it isn't we search in the opposite subarray

```
"""
    Use binary search to solve the problem
        basic implementation of binary search with a slight twist

    as mentioned in the problem, the array is rotated & we need to find an element in this array
        the key is to check if the left & right subarrays are sorted & if the target is in there
            if it is we search in that particular subarray
            if it isn't we search in the opposite subarray
    
    loop while left pointer <= right pointer
        calculate mid value
            if this is target, return mid index
        check if left pointer value <= mid value -- this means left subarray is sorted
            check if left value <= target <= mid value -- this is checking if the target is between these values
                if it is, check in left subarray
            if it isn't, value is in the right subarray, check in right subarray
        if the above condition is false -- it means right subarray is sorted
            check if mid value <= target <= right value -- this is checking if the target is between these values
                if it is, check in right subarray
            if it isn't, value is in the left subarray, check in left subarray

    loop until condition is invalidated & if result isn't returned in the loop, value isn't present in input
"""
```
