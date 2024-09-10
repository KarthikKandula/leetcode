class Solution:
    """
    NeetCode solution

        Use hashmap to keep a record of all values in input strs
            Use count (26 indexes for each letter from a to z) to record occurences for each value in strs
            add count to res & append the strs value if match

        return hashmap's values as result set 
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # defaultdict initializes an empty list for any unassigned values 

        # Loop thru input strs
        for s in strs:
            # Create an array of length 26 to record the count of each variable
            count = [0] * 26 # a ... z

            # Loop thru each letter in s
            for i in s:
                # append the count of each letter using ascii values
                count[ord(i) - ord('a')] += 1
                    # here if you subtract the ascii value of any letter with value of a, it always is less than or equal to 0 matching with the indexes of count
            
            # append the count array to res hashmap
            res[tuple(count)].append(s) # converting it to tuple, makes it hashable

        # return values of res hashmap
        return res.values()

    """
    My solution
    """
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = {}

    #     for s in strs:
    #         count = {}

    #         for i in s:
    #             count[i] = 1 + count.get(i, 0)
            
    #         # res[tuple(count)].append(s)
    #         if tuple(count) in res:
    #             res[tuple(count)].append(s)
    #         else:
    #             res[tuple(count)] = [s]

    #         print(count)
        
    #     print(res)

    #     return res.values()
        