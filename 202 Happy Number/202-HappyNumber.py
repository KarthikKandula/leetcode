class Solution:
    def isHappy(self, n: int) -> bool:
        # create set to track numbers already seen
        hist = set()

        # loop while True
        while True:
            square = 0 # create a square variable

            # loop for each digit in n -- convert as string to get each digit
            for i in str(n):
                # add squareroot of current digit to square
                square += int(i) ** 2
            
            # if square is 1 after above ops
            if square == 1:
                return True # we found a happy num, return True

            # if square is already in set, it's probably a cycle
            if square in hist:
                return False # we found a cycle, return False
            
            # add current value to set
            hist.add(square)

            # reassign square to n for next loop
            n = square