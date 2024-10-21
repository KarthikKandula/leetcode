# 621. Task Scheduler

1 possible solution for this problem  

## Method 1

To solve the task scheduling problem, we use both a heap and a queue. Follow these steps:

### Steps

1. **Count Task Occurrences**:
   - Count the occurrences of each task in the input array. This helps determine the frequency of each task that needs to be scheduled.

2. **Use a Max-Heap to Manage Task Counts**:
   - Insert the negative of each task count into a max-heap. This ensures that tasks with the highest remaining counts are always processed first.
   - Negating the counts transforms Python's `heapq` (which is a min-heap by default) into a max-heap.

3. **Use a Queue to Manage Task Cooldown**:
   - Create a queue to record tasks that are currently in their cooldown period (based on the given cooldown `n`).
   - Each entry in the queue stores the task’s count and the time when it can be re-added to the heap.

4. **Track Time**:
   - Initialize a variable `time` to keep track of the total time, which increments with each iteration (whether a task is processed or the CPU is idle).

5. **Process Tasks**:
   - Loop while the heap or queue contains tasks:
     - Increment the `time` variable by 1.
     - If there are tasks in the heap, pop the task with the highest count (since it's a max-heap).
     - Decrease its count (since it's been processed), and if it still has remaining instances, insert it into the queue along with the time it can be re-added to the heap (`current time + n`).

6. **Re-Add Tasks from the Queue to the Heap**:
   - Check the queue for any tasks that are eligible to be re-added to the heap based on the current time.
   - If any tasks have completed their cooldown, push them back into the heap.

7. **Return Total Time**:
   - Once all tasks have been processed, return the total time, as tracked by the `time` variable.

### Conclusion

This approach efficiently schedules tasks while respecting cooldown periods, using a max-heap and queue with a time complexity of O(n log n), where `n` is the number of tasks.


### Self Notes
To solve this problem, we can use a heap & queue, since a heap always has it's elements in sorted order, add & pop operations happen in log(n) time. count the occurences for each task in the input, insert only counts (values) into the heap -- negate them so it's max heap, create a queue -- to record values that will be inserted back into the heap, create a variable that keeps track of time. loop while heap or queue has values, increment time by 1 for every loop, works if we're currently running a task or staying idle. pop values from heap (running a task), add 1 to count (reducing the count since values are -ve), if count is not 0, insert into queue in format - [count, time at which this can be added back to heap (time +n)]. After this check if there are any values from queue that can be inserted back into heap at current time, insert them as necessary. at the end, return time variable value 


```
"""
   we use heap & queue to solve this problem
      count the occurences for each task in the input
      insert only counts (values) into the heap -- negate them so it's max heap
      create a queue -- to record values that will be inserted back into the heap
      create a variable that keeps track of time

   loop while heap or queue has values
      pop values from heap
         reduce count by 1 -- since using one time interval
         increment time by 1
         insert into queue if count is not 0 in format - [count, time this can be inserted back into heap (time + n)]
      check if first value in queue can be inserted at current time
         insert if true

   once loop is done, return time variable 
"""
```
