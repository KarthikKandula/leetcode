# 1046. Last Stone Weight

1 possible solution for this problem  

## Method 1

To solve this problem using a heap, follow these steps:

### Steps

1. **Use Python's Min-Heap as a Max-Heap**:
   - Python’s `heapq` implements a min-heap by default. To simulate a max-heap, negate all values when adding them to the heap.
   - This way, the smallest element in the min-heap corresponds to the largest element when negated.

2. **Initialize the Heap**:
   - Convert the given array of values by negating each element and heapify the array to create the heap.

3. **Iteratively Process the Heap**:
   - While the length of the heap is greater than 1:
     - Pop the two largest (most negative) elements.
     - Compare their absolute values.
     - If their difference is non-zero, push the negated result back into the heap.

4. **Return the Result**:
   - After processing, the heap will contain either one element or be empty.
   - If one element remains, return its absolute value; otherwise, return 0.

### Conclusion

This approach efficiently processes the elements using a heap, with a time complexity of O(n log(n)), where `n` is the number of elements in the heap.


### Self Notes
To solve this problem, we can use a heap, since a heap always has it's elements in sorted order, add & pop operations happen in log(n) time. python has minheap implementation -- for this problem we want the max heap, to handle this, we'll negate all values -- so it'll implement maxheap. loop while length of heap is greater than 1, pop two values from it & compare them, insert their difference if other than 0. by end of this loop, either 1 value or 0 values are in the heap. return accordingly


```
"""
   solve this problem using heap
      python has minheap implementation -- for this problem we want the max heap
      to handle this, we'll negate all values -- so it'll implement maxheap

   insert values into an array by negating the values & heapify it

   loop while length of heap > 1
      pop two values from heap
      insert their difference if values are not equal
   by the end of this loop, heap either has 1 value or 0

   return value from heap if heap has value else return 0
"""
```
