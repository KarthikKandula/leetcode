class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # array to collect results
        res = []

        # recursive function
        def matches(i, formed):
            # base conditions
            # if i reaches end
            if i == len(s):
                # it means, a possible solution has been formed
                # append to result
                res.append(formed)
                return # return after appending
            
            # loop thru each word in dict & check for matches
            for word in wordDict:
                # get length of the word
                wLen = len(word)

                # check if next word length chars are same as word
                if s[i:i + wLen] == word:
                    # if they are same, we found another match
                    # call the function to check for more matches, update the formed word
                    matches(i + wLen, word if formed == "" else formed + " " + word)
        
        # initial function call
        matches(0, "")

        # return result array
        return res
