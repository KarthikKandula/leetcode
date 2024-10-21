# 973. K Closest Points to Origin

1 possible solution for this problem  

## Method 1

To solve the problem using a heap, follow these steps:

### Steps

1. **Use Python's Min-Heap**:
   - Python’s `heapq` provides a min-heap implementation, which is suitable for our use case as it efficiently keeps elements in sorted order.
   - Both insertion and removal (`push` and `pop`) operations take O(log(n)) time.

2. **Calculate Distances and Store in an Array**:
   - For each point, calculate its Euclidean distance from the origin.
   - Store each point in the format `[distance, x, y]` in an array.

3. **Heapify the Array**:
   - Convert the array into a heap using Python’s `heapify` function. This organizes the array based on the calculated distances.

4. **Extract the k Closest Points**:
   - Loop for `k` iterations:
     - Pop the smallest element from the heap (which represents the closest point).
     - Append the `(x, y)` coordinates of this point to the result array.

5. **Return the Result Array**:
   - The result array will contain the coordinates of the `k` closest points.

### Conclusion

This approach efficiently finds the k closest points using a heap with a time complexity of O(n log(n)), where `n` is the number of points in the input.


### Self Notes
To solve this problem, we can use a heap, since a heap always has it's elements in sorted order, add & pop operations happen in log(n) time. python has minheap implementation, perfect for our current usecase. calculate distance for each point & store it in an array in format - [dist, x, y], heapify the array, loop for k times, pop from heap, append x & y coordinates to result array, return result array


```
"""
   solve this problem using heap -- python has minheap, that is perfect for the solution

   calculate distance for each point & store it in an array in format - [dist, x, y]

   heapify the array

   loop for k times
      pop from heap
      append x & y coordinates to result array

   return result array 
"""
```
