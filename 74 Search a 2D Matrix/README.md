# 74. Search a 2D Matrix

1 possible solutions for this problem  

## Method 1

This problem requires performing **binary search** twice: once to locate the row where the target value might exist and then again to search within that row.

1. **First binary search (find the row)**:
   - Treat the matrix as an array of rows. Perform binary search on the first element of each row to find the row where the target value could potentially exist.
   - This search works because each row is sorted, and the first element of each row is smaller than the last element.
2. **Second binary search (find the value in the row)**:
   - Once the correct row is found, perform a second binary search within that row to locate the target value.
   - Since each row is individually sorted, a binary search can efficiently determine if the value exists.
3. **Return result**:
   - If the target is found in the second binary search, return `True`. If not, return `False`.

This approach reduces the time complexity by leveraging binary search twice, making the solution more efficient than a simple linear search through the entire matrix.

### Self Notes
This problem is a nested binary search , implement binary search twice once to find the row in which target value exists & other to find the value in the row.
