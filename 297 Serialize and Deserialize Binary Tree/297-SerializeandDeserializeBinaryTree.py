# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    """
    use dfs pre-order traversal to serialize the tree
        indicate null nodes by N
    
    create an array to store node values -- makes it easy for append ops
    after implementing dfs pre-order traversal recursively

    convert array into string with , delimiters before returning
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = [] # array to hold preorder traversal on input tree

        # helper function to implement recursive dfs
        def dfs(curr):
            # check if curr node is valid
            if not curr:
                res.append('N') # if not, append N to array
                return # return from function -- since we want execution to stop

            # append curr value to res array
            res.append(str(curr.val))

            dfs(curr.left) # recursive call for left subtree
            dfs(curr.right) # recursive call for right subtree

        dfs(root) # initial helper function call

        # return in string format with , delimeter
        return ",".join(res)

    """
    use dfs pre-order traversal to deserialize the tree
    
    create an array to store node values -- makes it easy to access value
        split input string by ,'s
    create a count value that indicates current position in the above array

    create a helper function to implement dfs recursively
        if current position in array is N
            increment count value -- for future ops
            return None
        create a node with current position's value
            increment count value -- for future ops
        recursive call for left subtree
        recursive call for right subtree

        return node at the end

    return the node that is returned for first function call -- that is the root node
    """
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',') # split input string by , into an array
        self.i = 0 # variable to hold current position in vals array
        
        # helper function to implement recursive dfs
        def dfs():
            # check if current position is N -- means Null
            if vals[self.i] == 'N':
                self.i += 1 # increment count pointer to point to next value
                return None # return None
            
            # create node for current value
            node = TreeNode(int(vals[self.i]))
            self.i += 1 # increment count pointer to point to next value
            node.left = dfs() # recursive call for left subtree
            node.right = dfs() # recursive call for right subtree

            # return node created above
            return node

        # return node that is returned by helper function -- this is the return value for the root node
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))