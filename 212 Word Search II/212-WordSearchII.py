# define a class for TrieNode to implement Trie
class TrieNode:
    def __init__(self):
        # hashmap to store children information
        self.children = {} # stored in format char: TrieNode()
        self.isWord = False # represents if this node is an end of any word

    def addWord(self, word):
        curr = self # create a curr variable

        # loop thru input word
        for c in word:
            # check if current char in children hashmap
            if c not in curr.children:
                # if not, create node & assign to value
                curr.children[c] = TrieNode()

            # update curr to advance for next node
            curr = curr.children[c]

        # now, curr is at the last letter, update isWord parameter to True
        curr.isWord = True

class Solution:
    """
    this problem is similar to word search but here words are given to us
        need to find which words appear in board
    
    if we implement a recursive dfs function, we need to implement dfs for each word
        that multiplies it by the number of words given to us
    
    to implement it in a more efficient manner
        we can first create a trie for the words
        loop thru each position from the board & check if that value exists in the trie
            if it does, recursive call for adjacent nodes with the next node's value
            if it doesn't return from function 
                so essentially only hitting a position if it exists in the trie
                reduces on the number of recursive calls
    
    create a root node for trie
        add all words to trie

    loop thru all rows & colums
        recursively call helper function for each position in board

    create a helper function that implements dfs recursively
        input is row, column, trie's node that we're searching & the current string that matched from trie so far
        check if row, column are out of bounds
            return from function
        check if row, column exists in visited
            return from function
        check if current value in board exists in trie at current node
            return from function
        
        at this point in the program, it means we're in the right direction to find a word

        add current position to visited
        update node from trie to the new node
            since it matched with current board's position
        update word
            add current board's position to it
        if current node is marked as end of word
            add it to result
        
        recursively call for all 4 adjacent positions
        
        cleanup current position from visited -- for future recursion ops

    after all recursive functions return, result is in result set, return it as a list
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode() # create root node for trie

        # add words to Trie
        for w in words:
            root.addWord(w) # use function in Trie class to add words to Trie
        
        # create variables for row, cols, result & visited
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        # create helper function
        def dfs(r, c, node, word):
            # check if current position out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            
            # check if current position in visited
            if (r, c) in visited:
                return
            
            # print(r, c)

            # check if current value in board is not in node's children
            if board[r][c] not in node.children:
                return

            # if reached this point, means not out of bounds, not visited & in node's children -- going in right direction

            # add to visited
            visited.add((r, c))

            # update node value -- to make recursive calls
            node = node.children[board[r][c]]

            # update word value -- to make recursive calls
            word += board[r][c]

            # if node is end of word in trie -- add to result
            if node.isWord:
                res.add(word)

            # make recursive calls
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # cleanup visited -- for future recursive calls
            visited.remove((r, c))

        # call recursive function repeatedly
        for r in range(ROWS):
            for c in range(COLS):
                # check if current position is in root's children
                if board[r][c] in root.children:
                    dfs(r, c, root, "") # initial call for recursive function for each position

        # return result as list
        return list(res)
