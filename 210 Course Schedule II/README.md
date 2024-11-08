# 210. Course Schedule II

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given a list of courses with prerequisites and need to determine an order in which to take these courses. This problem can be represented as a directed graph, where each course is a node, and an edge from `Course A` to `Course B` indicates that `Course A` is a prerequisite for `Course B`. The problem boils down to checking for cycles and then performing topological sorting to find the correct order.

## Approach

### Key Idea
1. **Build a Graph Representation**: Use a hashmap to store each course and its list of prerequisites.
2. **Detect Cycles and Order Courses Using DFS**: Use DFS to check if we can complete each course without encountering a cycle. Additionally, add courses to an output list in the correct order once all prerequisites are satisfied.
3. **Track Visited and Processed Courses**: 
   - Use a `visited` set to detect cycles.
   - Use a `completed` set to avoid redundant processing for courses whose prerequisites have already been resolved.

### Step-by-Step Solution

1. **Build the Graph**:
   - Create a hashmap where each course points to a list of its prerequisites.
   - Populate this hashmap based on the prerequisites given in the problem.

2. **Define a Recursive DFS Helper Function**:
   - **Input**: Current course.
   - **Base Cases**:
     - If the course is already in the `visited` set, return `False` to indicate a cycle.
     - If the course is already in the `completed` set, return `True`, as it has already been processed and added to the order.
   - **Process the Current Course**:
     - Add the course to the `visited` set to mark it as being processed.
     - For each prerequisite of the course:
       - Recursively call the DFS helper function.
       - If any prerequisite returns `False`, propagate `False` to indicate a cycle.
     - After visiting all prerequisites:
       - Remove the course from `visited` to allow other recursive paths.
       - Add the course to the `completed` set, as it has now been fully processed.
       - Append the course to the output list, as all prerequisites have been satisfied, and it can now be taken.
     - Return `True` if all prerequisites were satisfied without cycles.

3. **Iterate Over All Courses**:
   - For each course, call the DFS helper function.
   - If any course returns `False`, return an empty list immediately, indicating that it is impossible to complete all courses due to a cycle.

4. **Return the Result**:
   - Reverse the output list to get the correct order, as courses are added in reverse order during DFS processing.
   - Return the output list if all courses can be completed; otherwise, return an empty list.

### Summary
- **DFS Logic**: The DFS traversal checks each course's prerequisites while tracking visited courses to detect cycles and establish an order.
- **Efficiency**: By using a `completed` set, we avoid redundant checks and optimize performance.
- **Output**: The function returns the order in which courses should be taken or an empty list if it is impossible to complete all courses.


### Self Notes

```
"""
  we can treat this problem as a graph traversal problem
    we can create a graph for every prereq given in the problem
    the goal is to make sure we can take every possible course by satisfying each prereq
    an added functionality is to return the order in which courses should be taken
      to account for this, we add to an output list whenever a course is satisfied 
      and record that course in a seperate set to make sure no other dfs path adds it to output

  create a hashmap with every course & populate the prereq's for each course
  create a set to take note of visited courses already -- helps in detecting cycles
  create a set to take note of prereq's satisfied courses already added to output
    helps not to add duplciate courses to output

  create a helper function to implement recursively
    input is a course
    if course is in visited
      return False
    if course is in prereq's satisfied set 
      return True
    
    if reaches this point, it means this is a new course we're visiting & should be validated
    add course to visited
    loop thru all prereq's this course has & recusively call each course
      if any course returns false, return false for entire function
    
    if reaches this point, it means no course returned false
    remove course from visited -- freeing up for other recursive paths
    add course to prereq's satisfied set, since all prereq'a are resolved
    add course to output list, since as of this point this course can be taken
    return True

  loop thru each course & recusively call for each call
    if any course returns false, return false for entire function
  
  in the end, return output list if we've not returned false anywhere else
"""
```

