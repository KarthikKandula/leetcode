# define a class for TrieNode to implement Trie
class TrieNode:
    def __init__(self):
        # hashmap to store children information
        self.children = {} # stored in format char: TrieNode()
        self.isEndWord = False # represents if this node is an end of any word

class Trie:

    """
    create root node for trie
    """
    def __init__(self):
        # create root node
        self.root = TrieNode()

    """
    to insert a word
        loop thru each letter
        check if it exists in that hashmap
            if it does, do nothing
            if it doesn't, create a new node & assign to the letter in hashmap
        update curr to move to next node
        in the end, change isEndWord value to True
    """
    def insert(self, word: str) -> None:
        curr = self.root # create a curr variable

        # loop thru input word
        for c in word:
            # check if current char in children hashmap
            if c not in curr.children:
                # if not, create node & assign to value
                curr.children[c] = TrieNode()
            
            # update curr to advance for next node
            curr = curr.children[c]

        # now, curr is at the last letter, update isEndWord parameter to True
        curr.isEndWord = True

    """
    to search a word
        loop thru each letter
        check if it exists in the hashmap
            if it doesn't, return False
        update curr to move to next node
        in the end, return isEndWord value -- of the last letter's node
    """
    def search(self, word: str) -> bool:
        curr = self.root # create a curr variable

        # loop thru input word
        for c in word:
            # check if current char in children hashmap
            if c not in curr.children:
                return False # if not, return False
            
            # update curr to advance for next node
            curr = curr.children[c]
        
        # return isEndWord value for the last letter in input word
        return curr.isEndWord

    """
    to check if any word starts with a prefix
        loop thru each letter
        check if it exists in the hashmap
            if it doesn't, return False
        update curr to move to next node
        in the end, return True -- if the false condition isn't hit, means all letters exist
    """
    def startsWith(self, prefix: str) -> bool:
        curr = self.root # create a curr variable

        # loop thru input prefix
        for c in prefix:
            # check if current char in children hashmap
            if c not in curr.children:
                return False # if not, return False
            
            # update curr to advance for next node
            curr = curr.children[c]
        
        # return True since all letters from prefix exists in Trie
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)