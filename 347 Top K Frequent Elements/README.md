# 347. Top K Frequent Elements

3 possible solutions for this problem

## Method 1

### Problem: Top K Frequent Elements

We can solve this problem by using a **hashmap** to count the frequency of elements and a **count array** to track the frequency of occurrences.

1. **Hashmap to count elements**:
   - First, use a hashmap to count how many times each element appears in the input array.
2. **Count array**:
   - Create a count array of size `len(nums) + 1` to track how many times each frequency occurs. We use `len(nums) + 1` because the indexes represent frequencies, and the highest possible frequency is `n` (if an element repeats `n` times). The extra space ensures we don't miss any element with the maximum frequency.
3. **Populate count array**:
   - Iterate through the hashmap, where the keys are the elements and the values are their frequencies. For each element, place it in the count array at the index corresponding to its frequency.
4. **Build the result array**:
   - Iterate through the count array in descending order (from highest frequency to lowest).
   - Append elements to a new result array as you find them in the count array.
   - Since you're looping in descending order, the most frequent elements will be added first.
5. **Stop when `k` elements are found**:
   - Once the result array reaches a length of `k`, return it as the answer.

This approach efficiently tracks element frequencies and retrieves the top `k` frequent elements in descending order of frequency.

### Self Notes
Use a hashmap to count elements
Use a count array (of size len(nums)+1), to keep record the amount of time elements repeat via indexes, this is done since if we create a count array of len(nums), and since indexes are numbered 0...n-1, we'll be missing out on the last number and if an array exists where a number repeats n times. So we'll add the +1 here to accomodate for that.
Iterate thru the count array in desc order, append to new result array as we find elements in indexes (since we're looping in desc order, the max elements will be found first), if length is as k, return result array 

```
"""
    NeetCode solution - o(n)

        Use a hashmap to count elements
        Use a count array (of size len(nums)+1), to keep record the amount of time elements repeat via indexes
        Iterate thru the count array in desc order, append to new result array, if length is as k, return result array 
"""
```

## Method 2 (Using heap)

### Problem: Top K Frequent Elements Using Heap

We can solve this problem by using a **hashmap** to count element frequencies and a **heap** to efficiently extract the top `k` frequent elements.

1. **Hashmap to count elements**:
   - First, iterate through the input array and use a hashmap to count how many times each element appears. The keys are the elements, and the values are their respective frequencies.
2. **Insert into heap**:
   - For each element in the hashmap, insert it into a heap as a tuple `(-count, value)`. 
     - We use `-count` because Python’s `heapq` is a **min-heap** by default, and negating the count allows us to treat it like a **max-heap** (i.e., larger counts will be at the top of the heap).
3. **Pop from heap `k` times**:
   - Pop the heap `k` times to get the top `k` most frequent elements. Each time you pop, you'll retrieve the element with the highest frequency (since we negated the counts earlier).
4. **Return result**:
   - Collect the `k` elements popped from the heap and return them as the result.

This approach ensures that we can efficiently retrieve the top `k` frequent elements by leveraging the properties of a max-heap.

### Self Notes
Use a hashmap to count elements
For all elements in hashmap, insert into heap in a way as (-count, value)
    -count since python implements minheap, so -ve'ing it makes it max heap
now, pop from heap k times

```
"""
    Another solution (using heap)

        Use a hashmap to count elements
        For all elements in hashmap, insert into heap in a way as (-count, value)
            -count since python implements minheap, so -ve'ing it makes it max heap
        now, pop from heap k times
"""
```

## Method 3 (My Solution)

Use a hashmap to record no. of times each value occurs  
Sort the hashmap's values in descending order  
get the k elements from sorted values & extract from hashmap those elements, put them in an array & return

