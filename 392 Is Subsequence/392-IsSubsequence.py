class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # create two pointers each at start of each string
        i, j = 0, 0

        # loop while each pointer is less than the length of it's string
        while i < len(s) and j < len(t):
            # compare if values are same
            if s[i] == t[j]:
                # if they are, increment both pointers values
                i += 1
                j += 1
                continue

            # this is the else condition, increment only j pointer value
            j += 1

        # return True is i pointer has reached end, means full string has been traversed
        return True if i == len(s) else False
