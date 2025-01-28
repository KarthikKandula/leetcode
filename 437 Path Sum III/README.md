# 437. Path Sum III

2 possible solution for this problem  


```
"""
    this problem can be solved using a variation of prefix sum
        usually used to identify problem types like
        Find a number of continuous subarrays/submatrices/tree paths that sum to target
        the basic idea is that
            maintain a continous value of sum until now
            for each sum, at each location, add sum to hashmap
            check if the continous value - target value exists in the hashmap
                if it does, it means by removing those combinations, we can get to target
                increment count by the value of diff from hashmap
                    means, those many ways we can form the total by removing combinations
"""
```

