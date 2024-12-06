# 2013. Detect Squares

1 possible solution for this problem  

### Self Notes


```
"""
    the first condition for a square to be formed by two different points is that they're diagonal to each other
        for diagonal points, the diff of x & y values is equal
        once we find a diagonal points, we need to find the other two points to complete forming a square
        to find these other points
            we can interchange x & y values from each points to see if they exist in hashmap
            ex: x1, y1 & x2, y2 (diagonal points found) --> x1, y2 & x2, y1 (new points to be found)
            if those points exist, we can mutiply their counts to get the no. of squares that can be formed
"""
```

