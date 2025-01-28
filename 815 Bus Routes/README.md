# 815. Bus Routes

1 possible solution for this problem  


```
"""
    This is a classic graph problem that uses bfs
        the twist in the problem is that need to use indexes as buses 
        since the index is the common point between buses
            also need to calculate the no. of hops required between indexes, helps to have a common value
        use sets to identify which buses & stops have been visited
        once visited a bus, add all the stops for that bus to q -- using input
            makes hopping between buses easier
            so, not only using a graph, also using the input array in the solution
        uses two data structures to efficiently get to the solution
"""
```

