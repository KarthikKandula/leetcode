# 76. Minimum Window Substring

1 possible solution for this problem

## Method 1

We can solve this using the **sliding window** approach with two hashmaps:

1. **Initialize two hashmaps**: One for each string to track the character counts.
2. **Window size**: The sliding window in the second string should have the same length as the first string since we are looking for a permutation.
3. **Check for matches**: As you iterate through the second string, compare the two hashmaps. If they match at any point, a permutation is found.
4. **Slide the window**: If the hashmaps don't match:
   - Add the character at the `right` pointer to the second hashmap.
   - Remove the character at the `left` pointer from the second hashmap.
   - Increment the `left` pointer to maintain the window size.
5. **Continue until the end**: Repeat this process until the `right` pointer reaches the end of the second string.

This approach efficiently finds a permutation of the first string in the second string by sliding a fixed-length window and updating character counts.

### Self Notes
To achieve this we can use the sliding window method approach. There are two inputs, take two hashmaps to keep track of counts of each input strings. while going thru the second string, window length is going to be the length of first string since we need to find a permutation of the first string, check if the hashmaps match at any point, if they do solution is found. if not keep going thru the string by adding the right pointer to second hashmap & removing the left pointer from second hashmap & incrementing left pointer value. Doing it until the end gives the solution. 

```
"""
    Use sliding window method to solve the problem
        In this case, window length is limited to the length of s1, since that's the area we're always going to look thru

    Use two hashmaps to keep count of occurences in each inputs

    loop thru the second input 
        check if both hashmaps are equal
        if they aren't, add right pointer value to second hashmap
        remove left pointer value from second hashmap
    
    keep doing it until the end 
        in the end compare both hashmaps one final time & return appropriate values
"""
```

## Method 2

To Be Learned

```
"""
    To Be Learned
"""
```