# 4. Median of Two Sorted Arrays

1 possible solution for this problem  

writeup later

## Method 1

This problem requires implementing a time-based key-value store where we can **set** and **get** values associated with timestamps. We’ll use **binary search** to efficiently retrieve the closest value to a given timestamp.

#### 1. **Set function**:
   - Store the key-value pair along with the timestamp. Since a key can have multiple values over time, store these values as an **array of arrays** where each entry is in the format: `[value, timestamp]`.
   - Example: `key: [[value1, timestamp1], [value2, timestamp2], ...]`
   - This allows us to maintain a history of values for each key, ordered by timestamp.
#### 2. **Get function**:
   - To retrieve the closest value for a given key and timestamp, use **binary search** since the timestamps for each key are stored in **descending order**.
   - Implement binary search to find the largest timestamp that is **less than or equal to** the given timestamp.
   - If a matching timestamp is found, return the corresponding value. If not, return the value associated with the closest timestamp.
#### 3. **Key points**:
   - Use binary search to ensure efficient lookup of the value based on the timestamp.
   - If no exact timestamp match is found, return the value that has the largest timestamp that is still less than or equal to the given timestamp.

This approach ensures that both setting and getting values are optimized, and binary search is used to retrieve values in a time-efficient manner.

### Self Notes
To achieve this we can use binary search, it's basic implementation with a twist

set function
we need to store the key value pair along with timestamp - store in way key:[value, timestamp], make it an array of arrays since there can be multiple values for each key

get function
we need to get the closest value to the timestamp for a key if it exists, we can use binary search cuz timestamps are guaranteed to be in descending order, hence implementing binary search is the most logical choice. An added thing is to get the closes value to the timestamp each time so we can return it at the end. 

```
set function
"""
    check if key already exists in store hashmap
        if it does, append to array
        if doesn't, create new key
"""

get function
"""
    use binary search to solve the problem
        since timestamps are always in descending order, all timestamps are going to be sorted since we're appending to the end in above set function
        hence we can use binary search to easily search the array

    basic binary search implementation
        only need to update the output variable since need to return closest value that less than or equal to input timestamp
"""
```
