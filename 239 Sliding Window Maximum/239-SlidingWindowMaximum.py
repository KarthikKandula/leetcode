class Solution:
    """
    Use sliding window approach to solve the problem
        Use deque to keep track of the highest number from a window
            deque - always orders the values by descending order
        Another important detail is to insert indexes into the deque rather than the actual values

    loop thru input array - using right pointer
        insert current right pointer index into deque
        before inserting check if there are any values less than the current value
            if there are pop them all out - in a loop

        after inserting current value
        check if the left most value in greater than left pointer - to adjust values in deque according to the current window
            if there are, pop those values out

        check if the right pointer has come to a position where we can start inserting into the output array
            if it is, insert the left most deque value into the output, since it's the highest

    loop thru the end of the string
        since we're updating output throughout the loop, return output as answer
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] # array to store output
        deq = collections.deque() # create a deque
        l, r = 0, 0 # initialize left pointer at start

        while r < len(nums):
            # check if there are values in deque if the right most value is less than current right pointer value
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop() # if it is, pop from deque

            # Append current value to deque
            deq.append(r)

            # check if left pointer is greater than left most deque value - to check if there are any values outside the current window in the deque
            if l > deq[0]:
                deq.popleft() # if there are, pop from deque

            # check if current right pointer is >= k - to check if we can add to output yet
            if (r + 1) >= k:
                output.append(nums[deq[0]]) # add the left most value to deque, since it's the max
                l += 1 # increment left pointer, to move window forward

            r += 1 # increment right pointer, to move window forward

        return output