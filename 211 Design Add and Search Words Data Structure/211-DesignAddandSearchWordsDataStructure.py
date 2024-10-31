# define a class for TrieNode to implement Trie
class TrieNode:
    def __init__(self):
        # hashmap to store children information
        self.character = {} # stored in format char: TrieNode()
        self.isWord = False # represents if this node is an end of any word

class WordDictionary:

    """
    create root node for trie
    """
    def __init__(self):
        self.root = TrieNode() # create root node

    """
    to insert a word
        loop thru each letter
        check if it exists in that hashmap
            if it does, do nothing
            if it doesn't, create a new node & assign to the letter in hashmap
        update curr to move to next node
        in the end, change isWord value to True
    """
    def addWord(self, word: str) -> None:
        curr = self.root # create a curr variable

        # loop thru input word
        for c in word:
            # check if current char in children hashmap
            if c not in curr.character:
                # if not, create node & assign to value
                curr.character[c] = TrieNode()
            
            # update curr to advance for next node
            curr = curr.character[c]
        
        # now, curr is at the last letter, update isWord parameter to True
        curr.isWord = True

    """
    use backtracking to solve search function
        we need to perform recursive backtracking for .'s since we have to consider all children nodes
        better to use recursive backtracking to implement searching for each child node
    
    create a helper function to implement recursive backtracking
        input to this function is the index from input word & the node to search
        loop for range index to end of input word
            if current letter is .
                loop thru all the nodes in current character hashmap
                recursive call for each node with next index
                    return True if any value is successful
                else return False
            if current letter is a letter
                check if it exists in hashmap
                    if it doesn't return false
                move pointer to next location
        in the end return the isWord value of last node

    make first recursive call for index 0 & root -- return value of this is search function's return value
    """
    def search(self, word: str) -> bool:

        # helper function to implement recursive searches
        def dfs(j, root):
            curr = root # create a curr variable

            # loop for range j & end of word
            for i in range(j, len(word)):
                c = word[i] # get char at ith index from word

                # if c is a . -> a wildcard
                if c == '.':
                    # need to check for each child node
                    for child in curr.character.values():
                        if dfs(i + 1, child): # recursive call for next index & current child node -- call made for all children
                            return True # return True even if one child returns True
                    return False # return False if no child returns True
                # if c is a letter 
                else:
                    # check if current char in children hashmap
                    if c not in curr.character:
                        return False # if not, return False
                    
                    # update curr to advance for next node
                    curr = curr.character[c]
            
            # return isEndWord value for the last letter in input word
            return curr.isWord
        
        # initial function call
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)