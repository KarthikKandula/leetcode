# 72. Edit Distance

1 possible solution for this problem  

### Self Notes


```
"""
   this is a dynamic programming problem
      at any possible moment, we're interacting with two indexes
         i - index of word1
         j - index of word2
      there are 3 possible values operations possible at any single location
         insert - (i, j + 1)
            we're inserting the value just before our i pointer in word1
            by performing this operation, we'll have to move j pointer since the word is matching
            i pointer still remains in same location since it has to be matched
         delete - (i + 1, j)
            we're deleting the value at i pointer in word1
            by performing this operation, move i pointer since letter from word1 is deleted, check next letter
            j pointer still remains in same location since it has to be matched
         replace - (i + 1, j + 1)
            we're replacing the value at i pointer to match with j
            since they're matching we can move both pointers
      at any time we're doing this operation we always get the min value since problem asks for min no. of operations
"""
```
