class Solution:
    """
    this is a slight twist on the valid palindrome problem
        we can at most delete one character from the string & check if the string is palindrome
        we can accomplish this by checking for valid palindrome string if there's a mismatch
            once a mismatch is triggered, we'll check by ignoring both the pointers
                increment i pointer keeping j at same place
                keeping i at same place increment j pointer
    """
    def validPalindrome(self, s: str) -> bool:
        # create two pointers on either ends
        i, j = 0, len(s) - 1

        # loop while both pointers are not same
        while i < j:
            # if there's a mismatch
            if s[i] != s[j]:
                # check if there's a palindrome, ignoring both the pointers
                left = self.checkPalindrome(s, i + 1, j)
                right = self.checkPalindrome(s, i, j - 1)

                # return True if either of those checks returns True
                return left or right
            
            # increment/decrement pointers
            i += 1
            j -= 1
        
        # return True if return isn't triggered above
        return True

    # helper function to check for valid palindromes
    def checkPalindrome(self, s, i, j):
        # loop while both pointers don't meet
        while i < j:
            # if there's a mismatch
            if s[i] != s[j]:
                # return False
                return False
            
            # increment/decrement pointers
            i += 1
            j -= 1
        
        # return True if return isn't triggered above
        return True
