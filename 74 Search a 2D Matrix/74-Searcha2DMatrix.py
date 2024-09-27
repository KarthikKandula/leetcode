class Solution:
    """
    This is a nested binary search problem
        implement binary search twice
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the length of rows & columns for easy access
        rows, cols = len(matrix), len(matrix[0])

        # start & end for first binary search
        start, end = 0, rows - 1

        # basic binary search while condition - while start <= end
        while start <= end:
            midRow = (start + end) // 2 # calculate the index of midrow

            # check if first index of midRow is greater than target
            if matrix[midRow][0] > target:
                end = midRow - 1 # if it is, decrease end pointer, since value in left subarrays
            # check if last index of midRow is less than target
            elif matrix[midRow][-1] < target:
                start = midRow + 1 # if it is, increase start pointer, since value in right subarrays
            else: # if none of the above conditions is true, target value is in the current row
                break # break current loop, since we need the row value for next binary search
        
        # calculate row value again from start & end pointers from above loop
        row = (start + end) // 2

        # start & end pointers for second binary search - naming l, r for differentiation purposes
        l, r = 0, cols - 1

        # basic binary search while condition - while l <= r
        while l <= r:
            mid = (l + r) // 2 # calculate mid value

            # check if mid value is greater than target
            if matrix[row][mid] > target:
                r = mid - 1 # if it is, decrease right pointer, since value in left subarray
            # check if mid value is less than target
            elif matrix[row][mid] < target:
                l = mid + 1 # if it is, increase left pointer, since value in right subarray
            else: # if none of the above conditions is true, target value is found
                return True # return true, as per the requirement
        
        # if the value isn't found, return false
        return False