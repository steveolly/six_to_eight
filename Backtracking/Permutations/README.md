# Permutations

## Problem Description

Write a function called `permutations(nums)` that returns all possible arrangements of the numbers in a list.

A permutation is an arrangement of elements in a particular order.

Each number must appear exactly once in every permutation.

Unlike combinations, the order of elements matters.

## Examples

**Example 1**

```python
permutations([1, 2, 3])
```

Expected output:

```python
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
```

**Example 2**

```python
permutations([1, 2])
```

Expected output:

```python
[
    [1, 2],
    [2, 1]
]
```

**Example 3**

```python
permutations([5])
```

Expected output:

```python
[
    [5]
]
```

The order of the results does not matter.

## Guidelines

1. Create an empty list called `result` to store all permutations.
2. Create an empty list called `current` to build each permutation.
3. Create a tracking structure to remember which elements have already been used.
4. Create a recursive helper function called `backtrack()`.
5. **Base case:** When the length of `current` equals the length of `nums`, save a copy of `current` in `result`.
6. Loop through every index in `nums`.
7. If an element has already been used, skip it.
8. Otherwise:
   - Append the element to `current`.
   - Mark its index as used.
   - Make the recursive call.
   - Remove the last element using `pop()`.
   - Mark its index as unused again.
9. Return `result`.

## Important Hints

- Think about why tracking indices is useful.
- Why should you reset an element's used status after recursion?
- Why is the base case based on `len(nums)` rather than a fixed number?
- Remember that `[1, 2, 3]` and `[2, 1, 3]` are different permutations.

## Constraints

- `1 <= len(nums) <= 6`
- All elements in `nums` are distinct.
- Do not use `itertools.permutations()`.
- Do not use built-in permutation-generating functions.
- Use recursion and backtracking.

## Concepts Being Tested

- Recursion
- Backtracking
- State tracking
- Boolean tracking arrays
- Permutations versus combinations
- Append and pop
- Base cases

## Your Task

Implement:

```python
def permutations(nums):
    pass
```

After solving, analyze:

1. What is the time complexity?
2. What is the auxiliary space complexity?
3. Why do we need to track used elements?
4. Why must we reset the tracking value after recursion?
5. How many permutations are possible when the input contains `n` distinct elements?
