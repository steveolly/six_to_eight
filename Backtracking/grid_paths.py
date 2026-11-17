def grid_paths(rows, cols, blocked):
    result = []
    current = []

    def backtrack(row, col):
        if (row + 1 == rows) and (col + 1 == cols):
            result.append("".join(current.copy()))
            return
        if (col + 1) < cols:
            if (row, col+1) not in blocked:
                current.append("R")
                backtrack(row, col+1)
                current.pop()

        if (row + 1) < rows:
            if (row + 1, col) not in blocked:
                current.append("D")
                backtrack(row + 1, col)
                current.pop()

        return result
    return backtrack(0, 0)


print(grid_paths(3, 2, {(1, 1)}))
