# Word Search in a Grid

## Problem Description

Write a function called `word_exists(board, word)` that determines whether a given word exists in a 2D grid of characters.

You can find the word by moving horizontally or vertically through adjacent cells.

You cannot:

- Move diagonally.
- Use the same cell more than once in a single word search path.

The word must be constructed using adjacent cells in the correct order.

## Example Board

```python
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
```

## Examples

**Example 1**

```python
word_exists(board, "ABCCED")
```

Expected output:

```python
True
```

**Example 2**

```python
word_exists(board, "SEE")
```

Expected output:

```python
True
```

**Example 3**

```python
word_exists(board, "ABCB")
```

Expected output:

```python
False
```

**Example 4**

```python
word_exists(board, "SFCSEE")
```

Expected output:

```python
True
```

## Guidelines

1. Get the number of rows and columns in the board.
2. Create a recursive helper function called `backtrack(row, col, index)`.
3. The parameters represent:
   - `row`: current row position.
   - `col`: current column position.
   - `index`: the position of the character currently being searched for in `word`.
4. **Base case:** If `index == len(word)`, the entire word has been found.
5. Check whether the current position is outside the board.
6. Check whether the current board character matches `word[index]`.
7. If either check fails, return `False`.
8. Mark the current cell as visited so it cannot be reused in the same path.
9. Explore the four possible directions:
   - Down: `(row + 1, col)`
   - Right: `(row, col + 1)`
   - Up: `(row - 1, col)`
   - Left: `(row, col - 1)`
10. If any direction successfully finds the remaining word, return `True`.
11. Restore the current cell before returning so other paths can use it.
12. Try starting the search from every cell in the board.

## Important Hints

- You can use a `visited` set to track visited cells.
- Alternatively, you can temporarily replace a visited board character with a special marker such as `"#"` and restore it afterward.
- Why must you restore the board after exploring a path?
- Why do we pass `index + 1` to the next recursive call?
- What happens when a row or column becomes negative?

## Constraints

- `1 <= rows, cols <= 6`
- `1 <= len(word) <= 15`
- The board contains uppercase and lowercase English letters.
- Do not use external libraries.
- Do not use built-in word-search functions.
- Use recursion and backtracking.

## Concepts Being Tested

- Recursion
- Backtracking
- 2D lists
- Row and column indexing
- Boundary checking
- Visited-state tracking
- Exploring multiple directions
- Restoring state

## Your Task

Implement:

```python
def word_exists(board, word):
    pass
```

After solving, analyze:

1. What is the time complexity?
2. What is the auxiliary space complexity?
3. Why can we not visit the same cell twice in one path?
4. Why do we restore the cell after recursion?
5. Why are there at most three forward choices after the first move?
