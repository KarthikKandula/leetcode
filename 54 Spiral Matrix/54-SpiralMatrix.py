class Solution:
    """
    this is an Array Matrix problem
        this can be solved using left, right, top, bottom pointers
        just have to be careful & smart on how to use the pointers as well as how to increment/decrement them

        if we write out the indexes of the supposed path, we observe a pattern on what to reduce when
            now implementing this pattern to code takes the 4 pointers
        
    create an array to store result

    create pointers
        left - points to left most index -- always 0
        right - points to right most index - max column 
        top - points to top most index in the matrix - always 0
        bottom - points to bottom most index - max row

    loop while left is less than right & top is less than bottom
        create a different loop to get values in the following order
            left -> right -- top most row
            top -> bottom -- right most col
            right -> left -- bottom most row
            bottom -> top -- left most col
        all the while incrementing/decrementing pointer values to take into effect the changes
    
    in the end return result array
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # create result array
        res = []

        # variables for tracking left & right pointers
        l, r = 0, len(matrix[0])
        # variables for tracking top & bottom pointers
        top, bot = 0, len(matrix)

        # loop while left is less than right & top is less than bottom
        while l < r and top < bot:
            # get values from left to right in top row
            for i in range(l, r):
                res.append(matrix[top][i])
            # since top row's values are extracted, increment top to account for that
            top += 1

            # get values from top to bottom in right most row
            for i in range(top, bot):
                res.append(matrix[i][r - 1])
            # since all values in right most row are extracted, increment right to account for that
            r -= 1

            # if left & right meet or top & bottom meet, end this loop
            if not (l < r and top < bot):
                break

            # get values from right to left in bottom row
            for i in range(r - 1, l - 1, -1): # -1 in end to get values in reverse order, l - 1 to include l value
                res.append(matrix[bot - 1][i])
            # since all values in bottom row are extracted, increment bottom to account for that
            bot -= 1

            # get values from bottom to top in left most row
            for i in range(bot - 1, top - 1, -1): # -1 in end to get values in reverse order
                res.append(matrix[i][l])
            # since all values from left most row are extracted, increment left to account for that
            l += 1
        
        return res
