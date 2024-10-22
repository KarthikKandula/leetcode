# 295. Find Median from Data Stream

1 possible solution for this problem  

## Method 1

To solve the problem of continuously calculating the median of a dynamic data stream, we employ two heaps:

### Steps

1. **Concept Overview**:
   - **Two Heaps**:
     - **Small Heap (Max-Heap)**: Contains the smaller half of the numbers.
     - **Large Heap (Min-Heap)**: Contains the larger half of the numbers.
   - The goal is to maintain two heaps such that:
     - All values in the `smallHeap` are less than or equal to the values in the `largeHeap`.
     - The size difference between the two heaps is at most 1.

2. **Adding Numbers**:
   - When a new number arrives:
     - Add it to `smallHeap` first. Since Python has only a min-heap, negate the values to simulate a max-heap.
     - Balance the heaps by moving the largest value from `smallHeap` to `largeHeap` (which is the smallest negative value after negating back).
   - If the size of `largeHeap` exceeds the size of `smallHeap`, move the smallest value from `largeHeap` back to `smallHeap`.

3. **Calculating the Median**:
   - If the heaps have an equal number of elements, the median is the average of the largest value from `smallHeap` and the smallest value from `largeHeap`.
   - If one heap has more elements than the other, the median is the root of the heap with the extra element.

### Key Points

- **Time Complexity**: Adding a number takes O(log n) due to heap operations. Retrieving the median takes O(1) since the heaps are always balanced.
- **Balancing Heaps**: The heaps are dynamically balanced as new numbers are added, ensuring that the difference in size between the heaps is at most 1.

### Conclusion

This approach efficiently maintains the median of a stream of numbers using two heaps, with add and median operations both handled in logarithmic and constant time, respectively.


### Self Notes
To solve this problem, we use a heap, since a heap always has it's elements in sorted order, add & pop operations happen in log(n) time. python has minheap implementation, so we negate the values to simulate a maxHeap.

to solve this problem we have to continously sort input nums are we receive, sorting a single heap continously & accesing values to calc median is too much work, to get around this problem, create two heaps -- small & large, smallHeap is a maxHeap, largeHeap is a minHeap, values in smallHeap will always be less than values in largeHeap, their length will only ever differ by 1 unit

```
__init__
"""
   to solve this problem we have to continously sort input nums are we receive
      sorting a single heap continously & accesing values to calc median is too much work
   to get around this problem
      create two heaps -- small & large
         smallHeap is a maxHeap
         largeHeap is a minHeap
         values in smallHeap will always be less than values in largeHeap
         their length will only ever differ by 1 unit
"""

addNum
"""
   add any input value to the smallHeap

   check if values in heaps are in order
      if smallHeap's max value is greater than largeHeap's min value -- swap them around
         pop from smallHeap
         insert into largeHeap
   
   check if heaps are balanced
      if length of any heaps is greater than 2 of other
         swap values around 
"""

findMedian
"""
   check if length of any heap is greater than other
      odd no. of values -- return value from greater heap
   if length is same
      return calculation -- smallHeap's max value + largeHeap's min value / 2
"""
```
