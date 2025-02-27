# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        # recursive function
        def sumDepth(nestList, depth):
            total = 0
            # loop for each value in nested list
            for eachVal in nestList:
                # check if it's an integer
                if eachVal.isInteger():
                    # if its not, add that value multiplied by the depth to total
                    total += (eachVal.getInteger() * depth)
                else: # if it's a list, we need it processed
                    # recursive call to process this list
                    total += sumDepth(eachVal.getList(), depth + 1)
            # return total at the end
            return total
        
        # first recursive function call with depth 1
        return sumDepth(nestedList, 1)
