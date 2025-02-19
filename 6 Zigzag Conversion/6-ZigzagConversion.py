class Solution:
    """
    This problem is all about figuring out the right algorithm in this point
        figuring out how the characters map to rows
        each row follows a specific increment pattern in the zigzag structure
        here the problem follows specific incrementals for each segment
            and indeed more modified incrementals for middle rows
            once able to see that, the solution is found
    """
    def convert(self, s: str, numRows: int) -> str:
        # base case
        if numRows == 1:
            return s
        
        # result variable
        res = ""

        # loop for each row in numRows
        for r in range(numRows):
            # calculate increment
            increment = 2 * (numRows - 1)

            # loop for each increment -- to get values for each row
            for i in range(r, len(s), increment):
                res += s[i] # add current value to result
                
                # if current row is one of middle rows, add extra letter
                if r > 0 and r < numRows - 1:
                    # if the last value in this segment is in bounds
                    if (i + increment) - (2 * r) < len(s):
                        # append to result
                        res += s[(i + increment) - (2 * r)]

        # return result
        return res

