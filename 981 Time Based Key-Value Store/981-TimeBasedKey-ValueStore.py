class TimeMap:

    # Class initializer
    def __init__(self):
        # Create hashmap to store keys & values
        self.store = {}

    """
    check if key already exists in store hashmap
        if it does, append to array
        if doesn't, create new key
    """
    # Function to set key:[value, timestamp]
    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key exists in hashmap
        if key in self.store:
            self.store[key].append([value, timestamp]) # Append value to key value
        else: # if doesn't exists
            self.store[key] = [[value, timestamp]] # Create new key:value pair

    """
    use binary search to solve the problem
        since timestamps are always in descending order, all timestamps are going to be sorted since we're appending to the end in above set function
        hence we can use binary search to easily search the array

    basic binary search implementation
        only need to update the output variable since need to return closest value that less than or equal to input timestamp
    """
    # Get values corresponding to key & timestamp
    def get(self, key: str, timestamp: int) -> str:
        # if key not in hashmap, return ''
        if key not in self.store:
            return ""

        # retrieve all values for this key into a variable
        keyVals = self.store[key]

        l, r = 0, len(keyVals) - 1 # left & right pointers
        out = "" # Create output variable

        # if no values exist for the key
        if not keyVals:
            return "" 

        # Run loop while left <= right
        while l <= r:
            mid = (l + r) // 2 # Get mid value

            # check if keyvalue < timestamp, it means value in right subarray 
            if keyVals[mid][1] < timestamp:
                l = mid + 1 # Increment left value
                # update output variable since we get the value immediately adjacent to input timestamp, especially if it's a lesser value - acc to reqs
                out = keyVals[mid][0]
            # If keyvalue is > timestamp
            elif keyVals[mid][1] > timestamp:
                r = mid - 1 # decrement right pointer
            else: # If keyvalue == timestamp
                return keyVals[mid][0] # Return value correspoinding to the timestamp

        # return most closest value if timestamp is not found
        return out



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)