class Solution:
    """
    Use two pointers

    Use two pointers to access two ends of the input string
        check if the value at a place is alphanumeric (use is alnum), skip if it is - do for both left & right pointer
        else compare the values
            if doesn't match -> return false (palindrome should have same values)
            if matches, proceed to next location
    """
    def isPalindrome(self, s: str) -> bool:
        # Create left & right pointers
        l, r = 0, len(s)-1

        # Loop while l < r
        while l < r:
            # Check if s[l] is alphanumeric
            if not s[l].lower().isalnum():
                l += 1 # if not, increment l - essentially ignoring non-alphanumeric chars
            # Check if s[r] is alphanumeric
            elif not s[r].lower().isalnum():
                r -= 1 # if not, decrement r - essentially ignoring non-alphanumeric chars
            # Compare s[l] & s[r]
            elif s[l].lower() != s[r].lower():
                return False # return False if s[l] != s[r]
            # if program reaches this point, s[l] == s[r], hence increase l & decrease r
            else:
                l+=1 # increment l
                r-=1 # increment r
        
        # Return true if return false in loop is not hit
        return True