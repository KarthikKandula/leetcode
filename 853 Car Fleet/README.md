# 853. Car Fleet

1 possible solution for this problem  

## Method 1

We can solve this problem using a **stack** and sorting the input to determine which cars meet and form a fleet.

1. **Sort the input**:
   - First, sort the array by the starting positions of the cars. This helps us understand the order in which the cars are on the road, from last to first.
2. **Process from last to first**:
   - Traverse the sorted array from the car at the furthest position to the car at the nearest position (i.e., from last to first). This ensures we process slower cars that might affect faster cars behind them.
3. **Fleet logic**:
   - The key logic is that a faster car catches up to a slower car ahead, and once caught, both cars move at the slower car's speed, effectively forming a fleet.
   - For each car, calculate the time it would take to reach the destination and push this time onto the stack.
4. **Compare speeds**:
   - After pushing the current car’s time onto the stack, compare the time of the last car (top of the stack) with the second last car in the stack:
     - If the last car's time is less than or equal to the second last car's time, the faster car will catch up to the slower car, forming a fleet. Pop the last car from the stack as it merges with the fleet ahead.
     - If the last car's time is greater, it means the car is slower and will not catch up, so it remains as its own fleet.
5. **Final result**:
   - Continue this process until all cars have been processed. The number of fleets will be the number of elements left in the stack.
   - Return the length of the stack, as it represents the total number of car fleets.

This approach ensures that we accurately track how many car fleets are formed, by comparing the speeds of cars from last to first and merging them when necessary.

### Self Notes
We can use stack and sort the input to solve the problem, the problem is to find out which cars meet on the road & become a fleet. to determine this, we need to sort the array, so we can know the order in which the cars start. Once sorted, go thru the sorted list from last to first. The essential logic in this problem is a faster car catches up to the slower car in front of it & both now go at the slower cars speed, so for this we always calculate the speed of the particular car we're currently looping and insert the speed in the stack. after inserting we compare the speeds of the latest & 2nd last element in the stack, if the last element speed is less than or equal to the 2nd last element, it means it's a faster car, it'll catch up to the slower car which will make them a fleet, we can pop it out of the stack. if the value is greater however, it means it's a slower car, takes more time hence it'll not catch up to the car. And since we're doing this in last to first order, we only have to compare the last two elements in a stack at any point since we'll do this in every loop & all the values will eventually be compared. Finally the no. of fleets will be in the stack, return the length of stack & answer is there

```
"""
   use stack & sort the input to solve the problem

   first combine the inputs position and speed to make them a single pair value

   loop thru the sorted pair array in descending order - better to move in descending order, easier to know which catch up
      calculate the speed of the particular car - how much time it takes to reach target
         append it to the stack
      check if the stack has any values that are faster than other values - if it's faster, it'll catch up to the slower car & they become a fleet, hence unnesessary in the stack
         check the last element - most recently inserted element 
         check the second last element - 2nd most recently inserted element 
               hence we need to check if length of stack is 2
         if the last elements value is less than or equal it means it's the faster car, it'll catch up to the second last element & they become a fleet
         Now we only have to check for the last & 2nd last since we'll be doing to for each element & don't have to check it in a loop

   keep going thru the input & the no. of fleets will be in the stack
"""
```
