class Solution:
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
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # combine position and speed into a single pair in an array - (position, speed)
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []  # stack to keep track of fleets

        # loop thru the newly created pairs in descending order
        for p, s in sorted(pair)[::-1]:
            tempSpeed = (target - p) / s # calculate the speed of this particular car

            stack.append(tempSpeed) # append the speed to stack

            # if length of stack is atleast 2 (to make the comparision) & if last element is faster than the previous element
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # pop the latest element

        # return length of stack as it has the number of fleets
        return len(stack)
