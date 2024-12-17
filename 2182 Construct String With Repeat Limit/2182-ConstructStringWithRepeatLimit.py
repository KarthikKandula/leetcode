class Solution:
    """
    Polished solution
        My solution in polished code

    can solve this problem using maxHeap & counter
        get the max value from heap in every loop 
            add the character to output max allowed times & see if it has to be inserted back into the heap
            if this value still has remaining count
                get the next value from heap
                add it once to the output, so as to not violate the repeatLimit
        by doing this we're reducing the no. of iterations
    """
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # build heap in format (-ASCII val, count)
        heap = [(-ord(char), count) for char, count in Counter(s).items()]        
        heapq.heapify(heap)

        # result array
        res = []

        # loop while heap has values
        while heap:
            # pop highest value from heap
            ordVal, count = heapq.heappop(heap)

            # convert ASCII value to character
            char = chr(-ordVal)

            # calculate the max no. of times this value can be used
            used = min(count, repeatLimit)

            # add highest value max no. of times to output
            res.append(char * used)

            # update count by decrementing used times
            count -= used

            # if there are still values to be used of this character, process the next character
            if count > 0:
                
                # if heap doesn't have any values, it means this value should be used again
                # repeat limit doesn't allow that, so break loop
                if not heap:
                    break

                # pop next highest value from heap
                nextOrdVal, nextCount = heapq.heappop(heap)

                # convert ASCII value to character
                nextChar = chr(-nextOrdVal)

                # insert the next value once since output needs to be lexographically high
                res.append(nextChar)

                # update next count by decrementing used times
                nextCount -= 1

                # insert next value if count is greater than 0
                if nextCount > 0:
                        # insert next value back into heap
                        heapq.heappush(heap, (nextOrdVal, nextCount))
                    
                # insert first value back into heap
                heapq.heappush(heap, (ordVal, count))

        # return a string of values joined from the array
        return "".join(res)

    """
    My solution
    """
    # def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    #     count = {}

    #     for c in s:
    #         count[c] = 1 + count.get(c, 0)
        
    #     # print(count)

    #     heap = []

    #     for x in count:
    #         heap.append((-(ord(x)), x, count[x]))
        
    #     heapq.heapify(heap)
    #     lastChar, counter = '', 0
    #     out = ""

    #     while heap:
    #         # print(heapq.heappop(heap))

    #         ordVal, currChar, charCount = heapq.heappop(heap)

    #         if currChar != lastChar:
    #             counter = 0

    #         # if current char is same as last character & count is at limit
    #         # skip that character & try for the next one
    #         if currChar == lastChar and counter == repeatLimit:
    #             if not heap:
    #                 break
    #             else:
    #                 newOrdVal, newCurrChar, newCharCount = heapq.heappop(heap)

    #                 out += newCurrChar
    #                 lastChar = newCurrChar
    #                 counter += 1

    #                 newCharCount -= 1

    #                 if newCharCount > 0:
    #                     heapq.heappush(heap, (newOrdVal, newCurrChar, newCharCount))
                    
    #                 heapq.heappush(heap, (ordVal, currChar, charCount))

    #                 continue

    #         out += currChar
    #         lastChar = currChar
    #         counter += 1

    #         charCount -= 1

    #         if charCount > 0:
    #             heapq.heappush(heap, (ordVal, currChar, charCount))

    #     return out
