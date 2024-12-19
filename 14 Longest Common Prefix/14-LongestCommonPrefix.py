class Solution:
    """
    can solve this problem using string logic
        compare two words at a time
            since the problem asks for prefix
            get the lowest length of both the words
            check if the words are equal for the lowest length & decrease one for each time
        after all words are looped thru, the common prefix is saved in output variable 
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # variable to store common prefix across words 
        # initialize with first word
        word = strs[0]

        # loop thru each letter checking if it's equal
        for i in range(1, len(strs)):

            # get the minimum length of current prefix & current word
            minLen = min(len(word), len(strs[i]))

            # loop for minLen in reverse order & compare strings, if not equal reduce by 1
            for j in range(minLen, -1, -1):
                # check if substrings are equal
                if word[:j] == strs[i][:j]:
                    # if equal, replace common prefix
                    word = word[:j]
                    break # break from inner loop since no longer need comparision

        # return common prefix across all words
        return word
