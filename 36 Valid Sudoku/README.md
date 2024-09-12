# 36. Valid Sudoku

1 possible solution for this problem

## Method 1

Use hashset to solve the problem, since sets are always unique, it's a good idea to use them in a hashmap  
This problem is essentially 3 different problems
* unique values in rows
* unique values in cols
* unique values in 3x3 boxes


Have a hashset each for rows, cols & 3x3 boxes.  
* Key structure for 3x3 boxes hashset is a bit different since we're considering all the values in a single 3x3 box as one hashset
* We use a tuple (r//3, c//3) as a key in 3x3 boxes hashset

Loop thru each value in nested loops, check if the current value is already in any of the hashsets, if exists return false. if not, insert the value in all 3 hashsets  

repeat until end

```
"""
    Use hashset to solve the problem
        Since sets are always unique, it's a good idea to use them in a hashmap
    
    Have a hashset for rows, cols & 3x3 boxes
        the key structure for 3x3 boxes hashset is a bit different since 
        we're considering all the values in a single 3x3 box as one hashset

        We're using a tuple (r//3, c//3) as a key in 3x3 boxes hashset

    Loop thru each value in nested loops
        check if the current value is already in any of the hashsets, if exists return false
        if not, insert the value in all 3 hashsets
"""
```

