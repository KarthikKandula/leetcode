class Solution:
    """
    this problem can be solved using frequency hashmap/array
        the only catch being, we need to calculate frequency counters for each word
        a slight twist would be to compress all words in words2 to a single max word
            aka if requirements are 'o', 'oo', then we'd only need 'oo' since 'o' is automatically satisfied
        once we generate the freq array via ascii values
        match these values against each value in words1
            only if all conditions are satisfied
            add to output array
        return output array
    """
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # create an array to get character frequency for words2 -- compressed into a single max word
        charfreq = [0] * 26

        # loop for every word in words2
        for word in words2:
            # array to record frequency for this word
            tempfreq = [0] * 26

            # loop for every character in word
            for c in word:
                # get the ascii value difference
                val = ord(c) - ord('a')
                tempfreq[val] += 1 # increment value for this val

                # get max value for final array
                charfreq[val] = max(charfreq[val], tempfreq[val])

            # reset max freq to intial state
            tempfreq = [0] * 26

        # create array to store result
        universalWords = []

        # loop for every word in words1
        for word in words1:
            # array to record frequency for this word
            tempfreq = [0] * 26

            # loop for every letter in this word
            for c in word:
                # get ascii diff value
                val = ord(c) - ord('a')
                tempfreq[val] += 1 # incrment value for this char
            
            # create a flag to indicate if this word is universal
            isUniversal = True

            # loop for 26 aka for every letter -- constant time
            for i in range(26):
                # if any letter has lower frequency than required
                if tempfreq[i] < charfreq[i]:
                    isUniversal = False # turn the flag to false
                    break # break out of the loop
            
            # check if this word is universal -- will be changed if not
            if isUniversal:
                # if it is, append to output array
                universalWords.append(word)

        # return output array
        return universalWords

