class Solution:
    """
    use Topological Sort to solve the problem
        entire problem is dependent on the order of alphabets as appeared in the input 
        and figuring out the difference in order & returning them in lexicographically increasing order
        to achieve this, if we first build out a graph in the order of how the letters appear
            then we can traverse thru the graph & easily create the order in which the letter appear
    
    to apply topological sort to this problem, we need to build an adjacency list first
    create an hashmap with all letters that appear in the input
    building adjaceny list
        we'll compare any two words at once
        get the minlength of the two words in consideration
        we check for the condition -- if the first appearing letter has length more than second with same prefix
            acc to the problem desc, this is invalid
            if this occurs, return empty string since an order can't be established
            since if the first word has more letters with same prefix it's not possible to establish a relationship
        now, loop thru the minlength of both words & compare each letter
        on the first mismatch, add the mismatch to adjacency list
            the letter from first word comes before letter from second word
            hence add letter from second word to the value in letter from first word
        
    create a visited hashmap -- empty at first
        a hashmap in this case since we have multiple conditions to take care in terms of visited
        two values 
            False -- means this value has already been visited, this is not bad necessarily
            True -- means this value is visited & in current path, this will help in finding cycles
            if not in hashmap -- means a new value
    
    create a result array

    create a helper function implemented recursively
        input is the letter
        check for base condition
            if this letter has already been visited
                return the value from visited hashmap
        if reaches this point, it means it hasn't been visited & is a new letter
        assign value true to this letter in visited set
        now loop for each neighbor in adjacency list for this letter
            recursively call for each neighbor
            if any neighbor returns true -- it means there's a cycle, we return true
        change value to false for this letter in visited set
            not in current path anymore
        append this letter to result array
    
    loop thru each char in adjacencylist 
        call recursive function for each char
        if any function returns true, it means there a cycle & we return ""
        since there's no possibility of a solution
    
    if a solution is possible we can return the reversed out result array converted to a string
        solution is in reversed order since appending to result array only after all neighbors are visited
        this is the Kahn's algorithm aka topological sort
    """
    def alienOrder(self, words: List[str]) -> str:
        # create adjacency list
        adjList = {c:set() for w in words for c in w}

        # build adjacency list
        for i in range(len(words) - 1):
            # get two words from input
            w1, w2 = words[i], words[i + 1]
            
            # get minlength between current two words
            minLength = min(len(w1), len(w2))

            # check if len of first word is greater than second word & if prefixes are same
            # this can't happen acc to problem desc
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            
            # now loop for minlength 
            for j in range(minLength):
                # if any word mismatches
                if w1[j] != w2[j]:
                    # add it to adjacency list
                    adjList[w1[j]].add(w2[j])
                    break # stop processing any other words since we only want first mismatches

        # create set
        visited = {} # format False: visited, True: visited & in current path (indicates a cycle)
        res = [] # create result set

        # helper function to implement recursive dfs
        def dfs(c):
            # base condition
            # check if this char is already in visited
            if c in visited:
                return visited[c] # return appropriate value from visited
            
            # assign visited for this char to True
            visited[c] = True # visited & in current path

            # loop for each neighbor in adjacency list
            for eachNei in adjList[c]:
                # recursive call for each neighbor
                if dfs(eachNei):
                    return True # if any neighbor returns True, we return true, found a cycle
            
            # update visited value to false
            visited[c] = False # just making it visited, removing from current path

            # add to result set after all ops are done & all neighbors visited
            res.append(c)
        
        # loop thru each character in adjacency list -- the order doesn't matter since this is topological sort
        for eachChar in adjList:
            if dfs(eachChar): # check if any function returns true, it means a cycle
                return ""
        
        # reverse the result array since it's topolofical sort, the last element is added first
        res.reverse()

        # return result array in string format
        return "".join(res)


