# Combination Sum

## Problem Description

Write a function called `combination_sum(candidates, target)` that finds all unique combinations of numbers from `candidates` that add up to `target`.

You can use the same candidate number multiple times.

However, combinations that contain the same numbers in a different order should not be returned as separate answers.

For example, `[2, 3, 3]` and `[3, 2, 3]` represent the same combination.

## Examples

**Example 1**

```python
combination_sum([2, 3, 6, 7], 7)
```

Expected output:

```python
[
    [2, 2, 3],
    [7]
]
```

**Example 2**

```python
combination_sum([2, 3, 5], 8)
```

Expected output:

```python
[
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5]
]
```

The order of the results does not matter.

## Guidelines

1. Create an empty list called `result` to store valid combinations.
2. Create a list called `current` to build each combination.
3. Create a recursive helper function called `backtrack()`.
4. Your helper function should track:
   - `remaining`: how much of the target is left.
   - `start`: the index from which you can select candidates.
5. **Base case:** When `remaining == 0`, you have found a valid combination. Save a copy of `current` in `result`.
6. Loop through the candidates starting from `start`.
7. Append the selected candidate to `current`.
8. Recursively call the helper function with the updated remaining target.
9. Remember that you can reuse the same candidate.
10. Undo your choice using `pop()` after the recursive call.
11. Return `result`.

## Important Hints

- Think carefully about whether your recursive call should use `i` or `i + 1`.
- Why do we need the `start` parameter?
- Why should we save `current.copy()` instead of just `current`?
- What happens when `remaining` becomes negative?

## Constraints

- `1 <= len(candidates) <= 20`
- `2 <= candidates[i] <= 40`
- All candidate numbers are distinct positive integers.
- `1 <= target <= 40`
- Do not use `itertools`.
- Do not use built-in combination-generating functions.
- Use recursion and backtracking.

## Concepts Being Tested

- Recursion
- Backtracking
- Reusing elements
- Preventing duplicate combinations
- Remaining-target tracking
- List copying
- Pruning unnecessary branches

## Your Task

Implement:

```python
def combination_sum(candidates, target):
    pass
```

After solving, analyze:

1. What is the time complexity?
2. What is the auxiliary space complexity?
3. Why do we use `start`?
4. Why can we reuse the same index during recursion?
5. What would happen if we used `i + 1` instead of `i`?
