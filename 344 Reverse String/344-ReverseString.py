class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # create left & right pointers pointing at either ends of input
        l, r = 0, len(s) - 1

        # loop while l & r don't meet
        while l < r:
            # perform inplace swap
            s[l], s[r] = s[r], s[l]

            # increment/decrement pointers
            l += 1
            r -= 1
