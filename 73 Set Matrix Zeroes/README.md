# 73. Set Matrix Zeroes

1 possible solution for this problem  

### Self Notes


```
"""
   NeetCode constant space solution

   to solve this problem in constant space
      we can use the first row & col as indicators for their respective row & cols
      until we run into a problem since [0][0] is common for both row & col
         we'll use a different variable to indicate for the first row
   
   loop thru matrix to mark first row/col to 0
      only other than for the first row, since we created a seperate variable for that
   
   loop thru matrix to update values 
      only looping from 1 -> end for row & cols
      handling 0th row & index seperate
   
   check if [0][0] value is 0
      this is the indicator for first column, if it is, update values
   
   check if 0th row flag is True
      this is the indicator for first row, if it is, update rows
"""

"""
   My O(m + n) solution

   The idea is to use two sets
      one for rows & one for cols to record which rows/cols need to be made 0's
      using sets since there will not be any duplicates
   
   loop thru matrix once to populate sets
   loop thru matrix again to update values based on values in sets
"""
```

