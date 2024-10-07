# 287. Find the Duplicate Number

1 possible solution for this problem  

## Method 1

We solve this problem using **Floyd's Tortoise and Hare** algorithm, typically used for detecting cycles in a linked list, but adapted for arrays based on the problem constraints.

#### 1. **Problem Understanding**:
   - The array contains **n + 1** integers, but the range of values is **[1, n]**.
   - We can treat the array as a linked list where each value in the array points to the index of its next "node."
   - The input guarantees that there is at least one duplicate.

#### 2. **Algorithm Overview**:
   - Use two pointers:
     - **Slow Pointer** (`slow`): Moves 1 step at a time.
     - **Fast Pointer** (`fast`): Moves 2 steps at a time.
   - Since the array contains a duplicate, the pointers will eventually meet, indicating a cycle.

#### 3. **Steps**:

1. **Initialize the Pointers**:
   - Set both `slow` and `fast` pointers to the start of the array (`nums[0]`).

2. **Detect the Cycle**:
   - Move `slow` by 1 step and `fast` by 2 steps until they meet.
   - When they meet, it confirms the presence of a cycle (due to the duplicate).

3. **Find the Duplicate**:
   - Initialize another pointer (`slow2`) at the beginning of the array.
   - Move both `slow` and `slow2` pointers 1 step at a time until they meet.
   - The meeting point is the duplicate number in the array.

4. **Return the Duplicate**:
   - Return the value where the two pointers meet.

#### 4. **Complexity**:
   - **Time Complexity**: **O(n)** - The algorithm runs linearly through the array.
   - **Space Complexity**: **O(1)** - Only a few variables are used.

By transforming the array into a conceptual linked list, we can efficiently find the duplicate using the Floyd's Tortoise and Hare approach.

### Self Notes
To achieve this we can use Floyd's Tortoise & Hare algorithm to solve the problem. The algorithm uses two pointers slow & fast, slow -- moves 1 position with each iteration, fast - moves 2 positions with each iteration. the algorithm says these two pointers will meet eventually within n iterations if there is a cycle in the list. time complexity is O(n).
Now the twist in this problem is that, the input is an array, also according to the problem statement array contains n + 1 integers but range is [1, n], so we can consider the array values a linked list & the integers themselves pointing to nodes i.e the index of it's value. Also the input will never spill out. 
With this consideration, we take the slow & fast pointer, at the location where these both meet, break the loop. Now take another slow pointer that starts at the beginning, now increment these both pointers one position until they meet. the place where they meet is the duplicate number in the array. return this number

```
"""
   use Floyd's Tortoise & Hare algorithm to solve the problem
      this uses two pointers - slow & fast
         slow -- moves 1 position with each iteration
         fast -- moves 2 positions with each iteration
      the algorithm says these two pointers will meet eventually if there is a cycle within n iterations
         time complexity is O(n)
   
   but this is a bit different since the input is an array
      according to the problem statement there will be n + 1 integers in the array but range is [1, n]
      which means we can consider a linked list of sorts & the integers themselves point to the index of it's value. 
      Also, the input will never spill out
   
   going with this consideration & in accordance with floyd's algorithm
      we take slow & fast pointer
         at the location where these pointers meet, we break the loop
   
      now take another slow pointer -- slow2 starts from beginning
         we move the slow pointer & slow2 pointer one location at a time
               slow pointer stays where it was
         at one particular point, these pointers are going to meet which is the duplicate number
   
   return the duplicate number where slow & slow2 meet
"""
```
