class Solution:
    """
    Use sliding window method to solve the problem
        A slight variation on the traditional sliding window problem

    Use a set to keep record of all the elements appeared previously in the set

    loop thru the input using the right pointer
        insert elements as they appear in the set - as long as they don't exist already in the set
        if they already exist, remove from set until the duplicate element has disappeared - via the left pointer
    
    In every iteration, insert the current right pointer value to set
        since already removing any duplicates above

    update the result length variable in each iteration & eventually the variable will have max substring value
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize set - to record the elements that appeared previously
        charSet = set()
        l = 0 # left pointer
        res = 0 # result variable

        # loop thru length of input s, also r is right pointer here
        for r in range(len(s)):
            # check if current right pointer value exists in set
            while s[r] in charSet:
                charSet.remove(s[l]) # if it exists, it's a duplicate, remove s[l] until s[r] doesn't appear in set also removing any char before the duplicate as well
                l += 1 # increment left pointer
            
            # Add current right pointer to set - since already removed any duplicates above
            charSet.add(s[r])

            # length of current substring
            tempMaxLength = r - l + 1 
            res = max(res, tempMaxLength) # get max length

        # return result value
        return res