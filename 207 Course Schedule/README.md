# 207. Course Schedule

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given a list of courses with prerequisites and need to determine if it is possible to finish all courses by satisfying each prerequisite. This problem can be represented as a directed graph, where each course is a node, and a directed edge from `Course A` to `Course B` indicates that `Course A` is a prerequisite for `Course B`. The problem boils down to detecting if there are any cycles in the graph.

## Approach

### Key Idea
1. **Build a Graph Representation**: Use a hashmap to store each course and its list of prerequisites.
2. **Detect Cycles Using DFS**: Use DFS to check if we can complete each course without encountering a cycle. A cycle would indicate that a course depends on itself (directly or indirectly), making it impossible to complete all courses.
3. **Track Visited Courses**: Use a set to keep track of the current path of visited courses to detect cycles.

### Step-by-Step Solution

1. **Build the Graph**:
   - Create a hashmap where each course points to a list of its prerequisites.
   - Populate this hashmap based on the prerequisites given in the problem.

2. **Define a Recursive DFS Helper Function**:
   - **Input**: Current course.
   - **Base Cases**:
     - If the course is already in the `visited` set, return `False` to indicate a cycle.
     - If the course has no prerequisites in the hashmap, return `True` as it can be taken freely.
   - **Process the Current Course**:
     - Add the course to the `visited` set to track the current path.
     - For each prerequisite of the course:
       - Recursively call the DFS helper function.
       - If any prerequisite returns `False`, propagate `False` to indicate that the course cannot be completed.
     - After visiting all prerequisites:
       - Remove the prerequisites from the hashmap for this course to mark it as processed.
       - Remove the course from the `visited` set to allow other recursive paths.
     - Return `True` if all prerequisites were satisfied without cycles.

3. **Iterate Over All Courses**:
   - For each course, call the DFS helper function.
   - If any course returns `False`, return `False` immediately as it indicates that not all courses can be completed.

4. **Return the Result**:
   - If all courses are processed without returning `False`, return `True` indicating that all courses can be completed.

### Summary
- **DFS Logic**: The DFS traversal checks each course's prerequisites while tracking visited courses to detect cycles.
- **Efficiency**: By marking courses as completed in the hashmap, we avoid redundant checks and optimize performance.
- **Output**: The function returns `True` if it is possible to complete all courses; otherwise, it returns `False` if any cycle is detected.


### Self Notes

```
"""
  we can treat this problem as a graph traversal problem
    we can create a graph for every prereq given in the problem
    the goal is to make sure we can take every possible course by satisfying each prereq
      
  create a hashmap with every course & populate the prereq's for each course
  create a set to take note of visited courses already -- helps in detecting cycles

  create a helper function to implement recursively
    input is a course
    if course is in visited
      return False
    if course has no prereq's in hashmap
      return True
    
    if reaches this point, it means this is a new course we're visiting & should be validated
    add course to visited
    loop thru all prereq's this course has & recusively call each course
      if any course returns false, return false for entire function
    
    if reaches this point, it means no course returned false
    remove prereq's for this course, since they're all cleared
    remove course from visited -- freeing up for other recursive paths
    return True

  loop thru each course & recusively call for each call
    if any course returns false, return false for entire function
  
  in the end, return true if we've not returned false anywhere else
"""
```

