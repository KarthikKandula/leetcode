# 332. Reconstruct Itinerary

1 possible solution for this problem  

update details later

## Method 1


### Self Notes

```
"""
   we can treat this as a graph traversal problem where each airport is a node
      each ticket represents a directed edge, forming a path between airports
      the goal is to find a valid Eulerian path starting from "JFK" 
      in lexicographical order to form the itinerary
   
   create a hashmap to represent the graph (adjacency list)
      use a sorted order to add destinations for each airport
      add destinations in reverse sorted order to allow efficient traversal using pop() 
   
   create an empty list to store the final itinerary
      initialize a helper function for depth-first search (DFS) traversal
      this DFS uses post-order insertion to build the itinerary

   create a helper function to perform DFS
      input is an airport (node) in the graph
      loop while the airport has destinations, removing each destination and calling DFS recursively
      after all reachable destinations from this airport are processed, add this airport to the itinerary

   begin DFS from "JFK" as the required starting point
      each airport is added to the itinerary only after all destinations are exhausted
      reversing the final itinerary gives the correct order
   
   by the end of DFS, the itinerary list contains the desired path in the correct order
"""

"""
   Neetcode solution 

   causing time exceeds error

   we can treat this as a dfs graph traversal problem
      the problem is to identify the order of airports to travel so that all the tickets would be used 
      they'd like the result in alphabetical order
      to achieve this we create an adjacency list & populate it
      before populating the adjacency list, sort the input, this'll take care of sending result in alphabetical order

   create an helper recursive dfs function
      check base conditions
         if length of result is equal to length of tickets input + 1
               since result length is always going to be equal to length of tickets + 1
         if src not in adjMap
               means this airport is a destination, there is no source flight from here
      
      now loop for the dest for this airport from adj list
         remove each dest airport from the list
         add the dest airport to result array
         call the function recursively
               if call response is true, a path is possibel & return true
         if not, add this dest airport back to list
         remove dest airport from result array
      return false in the end
   
   once all calls return, the itineray is in the result array
"""
```
