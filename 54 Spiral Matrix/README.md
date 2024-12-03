# 54. Spiral Matrix

1 possible solution for this problem  

### Self Notes


```
"""
   this is an Array Matrix problem
      this can be solved using left, right, top, bottom pointers
      just have to be careful & smart on how to use the pointers as well as how to increment/decrement them

      if we write out the indexes of the supposed path, we observe a pattern on what to reduce when
         now implementing this pattern to code takes the 4 pointers
      
   create an array to store result

   create pointers
      left - points to left most index -- always 0
      right - points to right most index - max column 
      top - points to top most index in the matrix - always 0
      bottom - points to bottom most index - max row

   loop while left is less than right & top is less than bottom
      create a different loop to get values in the following order
         left -> right -- top most row
         top -> bottom -- right most col
         right -> left -- bottom most row
         bottom -> top -- left most col
      all the while incrementing/decrementing pointer values to take into effect the changes
   
   in the end return result array
"""
```
