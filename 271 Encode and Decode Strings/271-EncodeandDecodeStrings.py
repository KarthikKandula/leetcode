class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = '' # Create an empty result string var

        # interate thru strs
        for s in strs:
            # for every index, find the length of word & add it to res string in format 'length#word'
            res += str(len(s)) + '#' + s

        # return res after loop is completed
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = [] # create an empty result array 
        i = 0 # Initialize a variable to keep track of starting positions

        # iterate while i is withing bounds
        while i < len(s):
            j = i # Create another variable to iterate thru the string to find common encode char - '#'
            
            # iterate thru the rest of the str to find first occuring '#'
            while s[j] != '#':
                j += 1 # increment j until loop is satisfied
            
            # Now, i has the starting index of number before word & j has the ending index of number
            # Get the length of word using string slice op, convert to int (since it's a number)
            l = int(s[i:j])

            # Get the word thru the length above & append it to res array 
            res.append(s[j+1:j+1+l])
            
            # initialze the end of word index to i to restart loop
            i = j+1+l

        # return result array
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))