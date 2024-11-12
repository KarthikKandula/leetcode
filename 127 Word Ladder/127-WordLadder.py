class Solution:
    """
    we can treat this as a shortest path problem in an unweighted graph
        each word can be thought of as a node in the graph
        edges connect words that differ by exactly one letter, forming neighbors
        the goal is to find the shortest path from the beginWord to endWord

    create a hashmap (neiMap) to store word patterns
        each pattern replaces one letter with '*' to generalize word connections
        this map allows us to find all words that can connect by changing a single letter

    add beginWord to wordList to ensure it’s part of the graph
        for each word in wordList, populate neiMap with all possible patterns
        each pattern maps to a list of words that match this pattern
    
    use a visited set to keep track of words already processed
        start with a queue initialized with the beginWord for BFS traversal
        initialize a result variable (res) starting at 1 to count transformation levels

    loop while the queue has elements
        track the length of the queue to process levels separately in BFS
        pop words from the queue and check if it matches endWord -- return res if so
        generate patterns from the popped word and use neiMap to find neighbors
        for each neighbor, if it hasn’t been visited, add to visited and queue

    increment result variable after each level
        if endWord is reached, res will hold the shortest transformation length
        if queue is exhausted without reaching endWord, return 0 -- no transformation possible
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endword is not in list -- there's no result to find
        if endWord not in wordList:
            return 0

        # create neighbors map -- with default dict list
        neiMap = defaultdict(list)

        # append begin word to word list -- since this is the start of the graph
        wordList.append(beginWord)

        # loop thru wordList & populate neiMap
        for eachWord in wordList:
            # loop for each location of the word -- to add wildcard char *
            for j in range(len(eachWord)):
                # form a pattern with wildcard char in each location
                pattern = eachWord[:j] + '*' + eachWord[j + 1:]
                neiMap[pattern].append(eachWord) # append this word for this pattern to hashmap
        
        # take a visited set -- to avoid visiting same element twice
        visited = set()
        # take a queue -- implementing in iterative bfs
        queue = deque()
        # take a result variable -- starting with 1 since beginWord is already in queue & visited
        res = 1

        # add beginWord to visited set & queue
        visited.add(beginWord)
        queue.append(beginWord)

        # loop while queue has elements
        while queue:
            # get length of queue at this level
            qLen = len(queue)

            # loop thru queue in levels
            for i in range(qLen):
                # pop from queue
                wordPop = queue.popleft()
                # if popped word is same as end word
                if wordPop == endWord:
                    return res # return result since we've found the target word
                
                # loop thru length of the popped word to form patterns to search hashmap
                for j in range(len(wordPop)):
                    # form a pattern with wildcard char in each location
                    pattern = wordPop[:j] + '*' + wordPop[j + 1:]
                    
                    # loop thru this word's neigbors & add to queue
                    for eachNei in neiMap[pattern]:
                        # check if this neighbor is already in visited 
                        if eachNei not in visited:
                            # add to visited 
                            visited.add(eachNei)
                            queue.append(eachNei) # add to queue -- will be processed in next iteration
            
            # increment result after processing a level
            res += 1
        
        # return 0, if there is no path to be found, will be triggered if not returned in above value
        return 0

