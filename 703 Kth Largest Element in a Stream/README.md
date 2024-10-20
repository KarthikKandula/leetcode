# 703. Kth Largest Element in a Stream

1 possible solution for this problem  

## Method 1

To find the k-th largest element in a collection using a heap, follow these steps:

### Steps

1. **Use a Min-Heap**:
   - A heap keeps its elements in sorted order, and both insertion and removal operations (`push` and `pop`) occur in O(log(n)) time.

2. **Create a Heap with Size k**:
   - Initialize a min-heap (size `k`) to store the k largest elements encountered so far.
   - The k-th largest element will always be at the root (index 0) of the heap.

3. **Heapify the Initial Array**:
   - Add elements to the heap one by one.
   - If adding a new element makes the heap size exceed `k`, remove the smallest element (located at index 0).

4. **Return the k-th Largest Element**:
   - The element at the root of the heap (index 0) will be the k-th largest element after processing all elements in the array.

### Conclusion

This approach efficiently finds the k-th largest element with a time complexity of O(n log(k)), where `n` is the number of elements and `k` is the size of the heap.


### Self Notes
To solve this problem, we can use a heap, since a heap always has it's elements in sorted order, add & pop operations happen in log(n) time. if we create a heap with k length, the kth element is always going to be in location 0. Create an array & heapify it, if adding new values makes the heap more than k, pop values from it. return value in location 0 for kth element.


```
__init__
"""
   we can solve this problem using heap
      maintain a heap of size k -- this will be a min heap
         i.e., values will be in ascending order
         so kth value will be in location 0

   create an array with input nums
   heapfiy this array

   check if heap has more than k values
      if it does, pop values from heap
"""

add
"""
   add input value to heap

   check if heap has more than k values
      if it does, pop values from heap
   
   return value in location 0 -- this is kth value
"""
```
