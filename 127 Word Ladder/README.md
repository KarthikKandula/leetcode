# 127. Word Ladder

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given two words, `beginWord` and `endWord`, along with a `wordList`. The task is to transform the `beginWord` to the `endWord` by changing only one letter at a time. Each transformed word must exist in the `wordList`, and the goal is to find the shortest transformation sequence. This can be visualized as finding the shortest path in an unweighted graph where each word is a node, and edges connect words that differ by exactly one letter.

## Approach

### Key Idea
1. **Use BFS for Shortest Path**:
   - Since we are looking for the shortest transformation, BFS is ideal for level-by-level exploration.
2. **Generate Patterns for Efficient Neighbor Lookup**:
   - By replacing each letter in a word with `*`, we can generate patterns that generalize word connections (e.g., `hot` → `*ot`, `h*t`, `ho*`). This allows efficient lookup of words that differ by only one letter.

### Step-by-Step Solution

1. **Create a Pattern-Based Neighbor Map (`neiMap`)**:
   - Add `beginWord` to `wordList` if it's not already there to ensure it's part of the graph.
   - Initialize a hashmap, `neiMap`, where each generalized pattern (like `*ot` for `hot`) maps to a list of words that match this pattern.
   - For each word in `wordList`, generate all possible patterns by replacing each letter with `*`, and store the word under each pattern in `neiMap`.

2. **Initialize BFS**:
   - Use a `visited` set to track words that have been processed to avoid cycles.
   - Initialize a queue with the `beginWord` and start the transformation count (`res`) at `1`.

3. **Perform BFS for Shortest Path**:
   - While the queue has elements:
     - Track the length of the queue to process each level separately in BFS.
     - For each word in the current level:
       - Dequeue the word and check if it matches `endWord`. If it does, return `res` as the shortest transformation length.
       - Generate all possible patterns for the current word.
       - For each pattern, use `neiMap` to find all neighboring words.
       - For each neighboring word:
         - If it has not been visited, mark it as visited and enqueue it for processing.
     - Increment `res` after processing each level, indicating the next transformation step.

4. **Return the Result**:
   - If `endWord` is reached, `res` will contain the shortest transformation length.
   - If the queue is exhausted without reaching `endWord`, return `0`, indicating that no transformation is possible.

### Summary
- **BFS Logic**: Using BFS ensures that the shortest path is found first by processing all transformations level by level.
- **Efficiency**: The `neiMap` allows efficient lookup of neighbors by pattern matching, reducing unnecessary comparisons.
- **Output**: The function returns the shortest transformation sequence length, or `0` if no transformation is possible.


### Self Notes

```
"""
   we can treat this as a shortest path problem in an unweighted graph
      each word can be thought of as a node in the graph
      edges connect words that differ by exactly one letter, forming neighbors
      the goal is to find the shortest path from the beginWord to endWord

   create a hashmap (neiMap) to store word patterns
      each pattern replaces one letter with '*' to generalize word connections
      this map allows us to find all words that can connect by changing a single letter

   add beginWord to wordList to ensure it’s part of the graph
      for each word in wordList, populate neiMap with all possible patterns
      each pattern maps to a list of words that match this pattern
   
   use a visited set to keep track of words already processed
      start with a queue initialized with the beginWord for BFS traversal
      initialize a result variable (res) starting at 1 to count transformation levels

   loop while the queue has elements
      track the length of the queue to process levels separately in BFS
      pop words from the queue and check if it matches endWord -- return res if so
      generate patterns from the popped word and use neiMap to find neighbors
      for each neighbor, if it hasn’t been visited, add to visited and queue

   increment result variable after each level
      if endWord is reached, res will hold the shortest transformation length
      if queue is exhausted without reaching endWord, return 0 -- no transformation possible
"""
```
