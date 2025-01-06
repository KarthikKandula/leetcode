class Solution:
    """
    This solution uses two pointers, prefix sum, dynamic state tracking
        the solution requires keeping track of the no. of moves required to move balls at any index
        to achieve this, we need to know the no. of balls to left & right & no. of moves those balls make
    
    take 4 variables that track
        balls - to left & right -- 2 variables
        moves - to left & right -- 2 variables
    
    loop thru the length of input
        simultaenously calculate the no. of balls & moves at any particular index from either side
            left to right --> i
            right to left --> n - 1 - i
                gives index of current right pointer from last
        add current location value to balls 
        add no. of balls to moves at every index
            simulating moves each ball for every index
        if we add both left & right values, we get the total moves required for that index
    """
    def minOperations(self, boxes: str) -> List[int]:
        # get length of input
        n = len(boxes)

        # create output array for length of input
        ops = [0] * n

        # variable for state tracking
        ballsLeft = 0 # tracks balls to the left of index
        movesLeft = 0 # tracks moves of all balls to the left of index
        ballsRight = 0 # tracks balls to the right of index
        movesRight = 0 # tracks moves of all balls to the right of index

        # loop for length of boxes -- aka for index
        for i in range(n):
            # left to right ops
            l = i # left pointer, same as i
            ops[l] += movesLeft # add moves until now to output array
            
            # compute moves for the next index
            ballsLeft += int(boxes[l]) # add current index balls to balls variable
            movesLeft += ballsLeft # add no. of balls to moves aka shifting each ball

            # right to left ops
            r = n - 1 - i # right pointer, same as n - 1 - i
            ops[r] += movesRight # add moves until now to output array

            # compute moves for the next index
            ballsRight += int(boxes[r]) # add current index balls to balls variable
            movesRight += ballsRight # add no. of balls to moves aka shifting each ball

        # return output array
        return ops
