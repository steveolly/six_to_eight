# Generate All Valid Parentheses

## Problem Description

Write a function called `generate_parentheses(n)` that generates all possible combinations of well-formed parentheses using exactly `n` pairs of parentheses.

A well-formed combination must follow these rules:

1. Every opening parenthesis `(` must have a matching closing parenthesis `)`.
2. A closing parenthesis must never appear before its matching opening parenthesis.
3. The total number of opening and closing parentheses must each equal `n`.

## Examples

**Example 1**

```python
generate_parentheses(1)
```

Expected output:

```python
["()"]
```

**Example 2**

```python
generate_parentheses(2)
```

Expected output:

```python
["(())", "()()"]
```

**Example 3**

```python
generate_parentheses(3)
```

Expected output:

```python
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

The order of the results does not matter.

## Guidelines

1. Create an empty list called `result` to store all valid combinations.
2. Create a list called `current` to build the parentheses combination.
3. Create a recursive helper function called `backtrack()`.
4. Keep track of:
   - `open_count`: number of opening parentheses used.
   - `close_count`: number of closing parentheses used.
5. **Base case:** When the length of `current` reaches `2 * n`, save the completed combination in `result`.
6. You can add an opening parenthesis if `open_count < n`.
7. You can add a closing parenthesis only if `close_count < open_count`.
8. After each recursive call, undo the last choice using `pop()`.
9. Return the result.

## Constraints

- `1 <= n <= 8`
- Do not use `itertools`.
- Do not generate every possible string and filter invalid ones afterward.
- Use recursion and backtracking.
- Use a list to build the current combination.

## Concepts Being Tested

- Recursion
- Backtracking
- Base cases
- Conditional branching
- Append and pop
- Valid-state checking
- Call-stack tracing

## Your Task

Implement:

```python
def generate_parentheses(n):
    pass
```

After solving, analyze:

1. What is the time complexity?
2. What is the auxiliary space complexity?
3. Why is `close_count` never allowed to exceed `open_count`?
4. Why do we use `pop()` after each recursive call?
