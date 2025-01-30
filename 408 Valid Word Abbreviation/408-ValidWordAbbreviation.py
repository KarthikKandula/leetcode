class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # create two pointers, one for each string
        i, j = 0, 0

        # get lengths of word & abbr
        w = len(word)
        a = len(abbr)

        # loop while each pointer is in bounds
        while i < w and j < a:
            # if current char is a digit -> get all digits
            if abbr[j].isdigit():
                num = 0 # temp variable to store num for now

                # if starting digit is 0 -> not valid
                if num == 0 and abbr[j] == '0':
                    return False # return False

                # get all digits 
                while j < a and abbr[j].isdigit():
                    num = (num * 10) + int(abbr[j])
                    j += 1 # increment j pointer for the next digit

                # increment i pointer by the no. of digits
                i += num

            # if current char is a letter
            else:
                # compare current letters
                if word[i] != abbr[j]:
                    return False

                # increment i & j pointers
                i += 1
                j += 1

        return i == w and j == a
