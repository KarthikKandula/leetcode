class Solution:
    """
    Use sliding window method to solve the problem

    The entire problem relies on the formula 
        current length - count of max appearing value <= k (acceptable char changes)

    Use a hashmap to keep count of the elements appearing in the input

    loop thru the input using the right pointer
        update count of elements in hashmap as they appear 
        check if the formula holds up
            if it doesn't - move the left pointer & decrement the count in hashmap
            if it does - update the result value

    by end of the loop, eventually the result variable will have the answer
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # hashmap to keep track of alphabet counts
        l = 0 # initialize left pointer
        res = 0 # result variable

        # loop thru length of input s, also r is right pointer here
        for r in range(len(s)):
            # increment count of current right pointer value
            count[s[r]] = 1 + count.get(s[r], 0)
            # length of current iteration
            # tempLength = r - l + 1

            # check if current length - max occuring value is less than or equal to k 
            while (r - l + 1) - max(count.values()) > k:
                # if not, reduce the count of left pointer value
                count[s[l]] -= 1
                l += 1 # increment left pointer

            # update max length result variable with current length (if greater)
            res = max(res, r - l + 1)

        # return result
        return res

    """
    Use sliding window method to solve the problem

    The entire problem relies on the formula 
        current length - maxFrequency <= k (acceptable char changes)

    Use a hashmap to keep count of the elements appearing in the input
        slight modification is to create a new variable for maxFrequency

    loop thru the input using the right pointer
        update count of elements in hashmap as they appear 
        update maxFrequency with the current value of right pointer - eventually the value will have max value
        check if the formula holds up
            if it doesn't - move the left pointer & decrement the count in hashmap
            if it does - update the result value

    by end of the loop, eventually the result variable will have the answer
    """
    # def characterReplacement(self, s: str, k: int) -> int:
    #     count = {} # hashmap to keep track of alphabet counts
    #     l = 0 # initialize left pointer
    #     res = 0 # result variable
    #     maxF = 0 # variable for max frequency

    #     # loop thru length of input s, also r is right pointer here
    #     for r in range(len(s)):
    #         # increment count of current right pointer value
    #         count[s[r]] = 1 + count.get(s[r], 0)
    #         # Update max freq variable, if current right pointer value count is greater, it stays in there
    #         maxF = max(maxF, count[s[r]])

    #         # check if current length - max frequency value is less than or equal to k 
    #         while (r - l + 1) - maxF > k:
    #             count[s[l]] -= 1 # if not, reduce the count of left pointer value
    #             l += 1 # increment left pointer 

    #         # update max length result variable with current length (if greater)
    #         res = max(res, r - l + 1)

    #     # return result
    #     return res
