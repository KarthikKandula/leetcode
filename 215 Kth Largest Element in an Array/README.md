# 215. Kth Largest Element in an Array

1 possible solution for this problem  

need to learn quick select solution

## Method 1

To solve the problem using a heap, follow these steps:

### Steps

1. **Use Python's Min-Heap**:
   - Python’s `heapq` provides a min-heap implementation, suitable for maintaining the smallest elements efficiently.
   - Both insertion and removal (`push` and `pop`) operations take O(log(n)) time.

2. **Initialize a Heap of Size k**:
   - Insert the first `k` elements from the input array into the heap.
   - This will create a min-heap that keeps track of the k largest elements encountered so far.

3. **Process the Remaining Elements**:
   - For each element in `nums` beyond the first `k`:
     - Compare it with the smallest element in the heap (the root of the min-heap).
     - If the current element is greater than the smallest element:
       - Remove the smallest element using `heapq.heappop()`.
       - Insert the current element using `heapq.heappush()`.

4. **Final State of the Heap**:
   - The heap now contains the k largest elements from the input array.

5. **Result**:
   - Depending on the problem requirements, the result may be the smallest element in the heap (which is the k-th largest element) or the entire heap representing the k largest elements.

### Conclusion

This approach efficiently maintains the k largest elements using a min-heap with a time complexity of O(n log(k)), where `n` is the total number of elements and `k` is the size of the heap.


### Self Notes
To solve this problem, we can use a heap, since a heap always has it's elements in sorted order, add & pop operations happen in log(n) time. python has minheap implementation, perfect for our current usecase. implement a heap with length k, insert k elements from input into heap, for every other element in nums, check if it is greater than lowest element in heap, if it is, replace that element by popping & pushing into heap


```
"""
   Alternate efficient coded solution

   use heap to solve the problem
      we'll implement a heap with length k
      insert k elements from input into heap
      for every other element in nums, check if it is greater than lowest element in heap
         if it is, replace that element by popping & pushing into heap
"""

"""
   My solution

   create a new array same as input nums
   heapify this new array
   run a loop for the length of (length of heap - k) + 1
      continously pop from heap
   
   last popped value is the kth largest element
"""
```
