class Solution:
    """
    can solve this using string functions & two pointers
        use split() to get all words in a list
        use two pointers to loop thru the words in opposite directions
            interchange words at i, j location
            decrement both pointers to look at next set of words
        in the end, return a string joining all words with space in btwn
    """
    def reverseWords(self, s: str) -> str:
        # split words using split() function, splits it along spaces
        words = s.split()

        # create i, j pointers at opposite sides
        i, j = 0, len(words) - 1

        # loop while i is less than j
        while i < j:
            # replace words at i, j location
            words[i], words[j] = words[j], words[i]

            j -= 1 # decrement j pointer
            i += 1 # increment i pointer

        # return a string formed by joining string in words array with a space
        return " ".join(words)

    """
    can solve this problem using two pointers
        we need to skip any extra spaces found at the start, end & in between words
            if both pointers are pointing at a space, it's an extra space, ignore it
        we need to get all words
            as soon as both pointers hit anything other than a space, advance only the j pointer until a space is found
        once a space is found, get everything between j & i pointer
            it's a new word, append to result
        reassign both pointers to the position after j space
    
    by the end, reversed string is in result variable
    """
    # def reverseWords(self, s: str) -> str:
    #     # create i & j pointers
    #     i, j = len(s) - 1, len(s) - 1

    #     # create result variable
    #     res = ""

    #     # loop while j pointer is greater than 0
    #     while j >= 0:
    #         # if i, j are spaces, advance both of them
    #         if s[i] == ' ' and s[j] == ' ':
    #             i -= 1
    #             j -= 1
    #             continue
            
    #         # if i, j are letters, keep advancing j until space is found
    #         while j >= 0 and s[i] != ' ' and s[j] != ' ':
    #             j -= 1
            
    #         # append newly found word to result, changing logic to see if result is already initialzied for adding spaces
    #         if res:
    #             res += " "
    #             res += s[j + 1:i + 1] 
    #         else:
    #             res += s[j + 1:i + 1] 

    #         # decrement j pointer
    #         j -= 1
    #         i = j # reassign i pointer at the same location as j

    #     # return result in the end
    #     return res
