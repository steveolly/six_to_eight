# N-Queens Problem

## Problem Description

Write a function called `solve_n_queens(n)` that solves the N-Queens problem.

The goal is to place `n` queens on an `n x n` chessboard so that no two queens attack each other.

In chess, a queen can attack another queen if they are in the same:

- Row
- Column
- Diagonal

Your task is to return every possible valid board arrangement.

Represent:

- `"Q"` as a queen.
- `"."` as an empty cell.

## Examples

**Example 1**

```python
solve_n_queens(1)
```

Expected output:

```python
[
    ["Q"]
]
```

**Example 2**

```python
solve_n_queens(2)
```

Expected output:

```python
[]
```

**Example 3**

```python
solve_n_queens(4)
```

Expected output:

```python
[
    [
        ".Q..",
        "...Q",
        "Q...",
        "..Q."
    ],
    [
        "..Q.",
        "Q...",
        "...Q",
        ".Q.."
    ]
]
```

The order of the solutions does not matter.

## Guidelines

1. Create an `n x n` board filled with `"."`.
2. Create an empty list called `result` to store valid board arrangements.
3. Create tracking sets for:
   - Occupied columns.
   - Occupied diagonals.
   - Occupied anti-diagonals.
4. Create a recursive helper function called `backtrack(row)`.
5. **Base case:** If `row == n`, all queens have been successfully placed.
6. Convert the board into a list of strings and save it in `result`.
7. Loop through every column in the current row.
8. For each position, check whether:
   - Its column is occupied.
   - Its diagonal is occupied.
   - Its anti-diagonal is occupied.
9. If the position is safe:
   - Place a queen.
   - Add its column and diagonal identifiers to their tracking sets.
   - Recursively move to the next row.
10. After recursion:
    - Remove the queen.
    - Remove its identifiers from the tracking sets.
11. Return all valid solutions.

## Important Hints

For a position `(row, col)`:

- Column identifier: `col`
- Main diagonal identifier: `row - col`
- Anti-diagonal identifier: `row + col`

Positions sharing the same diagonal have the same `row - col`.

Positions sharing the same anti-diagonal have the same `row + col`.

You only need to place one queen per row, so you do not need to track occupied rows separately.

## Constraints

- `1 <= n <= 9`
- Do not use external libraries.
- Do not use a precomputed list of solutions.
- Do not use brute-force generation of every possible board.
- Use recursion and backtracking.
- Use sets to efficiently check occupied columns and diagonals.

## Concepts Being Tested

- Recursion
- Backtracking
- 2D lists
- Sets
- Diagonal mathematics
- State management
- Constraint checking
- Search-space pruning

## Your Task

Implement:

```python
def solve_n_queens(n):
    pass
```

After solving, analyze:

1. What is the time complexity?
2. What is the auxiliary space complexity?
3. Why do we use `row - col` for one diagonal?
4. Why do we use `row + col` for the other diagonal?
5. Why do we remove a queen after the recursive call?
6. Why don't we need to check whether another queen is in the same row?
