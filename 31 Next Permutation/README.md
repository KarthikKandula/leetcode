# 31. Next Permutation

1 possible solution for this problem  

# Understanding Permutations and Next Lexicographical Order

## Example: Permutations of `[1, 2, 3]`

1. `[1, 2, 3]` - Start with the smallest (lexicographically first)
2. `[1, 3, 2]`
3. `[2, 1, 3]`
4. `[2, 3, 1]`
5. `[3, 1, 2]`
6. `[3, 2, 1]` - End with the largest (lexicographically last)

---

### Observations:

- The **rightmost part** of the permutation changes more frequently than the **leftmost part**.
- This is why **analyzing from the right** is key to finding the next permutation.

---

## Structure of Permutations and Descending Suffixes:

1. **Lexicographical Order**:
   - Permutations are arranged in **lexicographical (dictionary) order**.
   - The **rightmost part of the array** is the "fastest-changing" part, while the **leftmost part changes the slowest**.

2. **Role of the Rightmost Portion**:
   - The **rightmost portion** determines the smallest possible changes that can be made to form the next permutation.
   - To get the next lexicographically larger permutation, you change the **smallest possible part** of the array to keep it as close to the current permutation as possible.

---

## Key Insight:

- The **suffix of the array** (from the rightmost side) forms a **descending sequence** in the largest possible subarray.
- This descending suffix represents the **"last" portion** of the current permutation.

---

### Steps to Find the Next Permutation:

1. **Identify the Rightmost Element**:
   - Find the **rightmost element** (`nums[i]`) that **breaks the descending order** (i.e., the first element smaller than its neighbor to the right).

2. **Swap**:
   - Swap it with the **smallest larger element** in the descending suffix.

3. **Reverse the Suffix**:
   - Reverse the suffix to get the **smallest order**.

---

### Self Notes

Example: Permutations of [1, 2, 3]:

[1, 2, 3]  # Start with the smallest (lexicographically first)
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]  # End with the largest (lexicographically last)

Notice that as you move through these permutations:

The rightmost part changes more frequently than the leftmost part.
This is why looking from the right is the key to finding the next permutation.


Let’s analyze how permutations are structured in terms of descending suffixes:

Permutations are arranged in lexicographical (dictionary) order.
the rightmost part of the array is the "fastest-changing" part, while the leftmost part changes the slowest.
The rightmost portion of the array determines the smallest possible changes that can be made to form the next permutation
To get the next lexicographically larger permutation, you want to change the smallest possible part of the array to ensure it remains as close to the current permutation as possible


Key Insight:
The suffix of the array (from the rightmost side) forms a descending sequence in the largest possible subarray.
This descending suffix represents the "last" portion of the current permutation.
To find the next permutation, we:
Identify the rightmost element (nums[i]) that "breaks" the descending order (the first element that is smaller than its neighbor to the right).
Swap it with the smallest larger element in the descending suffix.
Reverse the suffix to get the smallest order.



```

```

