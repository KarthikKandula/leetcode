class Solution:
    """
    we can solve this problem using two pointers & string
        use pointer i to loop from the back to find the first letter
        from the same position loop with j until find a space
        difference between i & j is the length of last word
    """
    def lengthOfLastWord(self, s: str) -> int:
        # create i pointer
        i = len(s) - 1

        # loop while i is a space
        while s[i] == ' ':
            i -= 1

        j = i # assign i value to j

        # loop while j is a letter
        while j >= 0 and s[j] != ' ':
            j -= 1

        # return difference of i & j
        return i - j

    """
    split input around a space
        find the last word that isn't a space & return it's length
    """
    # def lengthOfLastWord(self, s: str) -> int:
    #     words = s.split(' ')

    #     for r in range(len(words) - 1, -1, -1):
    #         if words[r]:
    #             return len(words[r])
