def solve_n_queens(n):
    if n <= 0:
        return []
    possible_results = []
    board = [["." for _ in range(n)] for _ in range(n)]
    occupied_cols = set()
    occupied_diagonal = set()
    occupied_anti_diagonal = set()

    def backtrack(row):
        if row == n:
            possible_results.append(["".join(r) for r in board])
            return

        for col in range(n):
            diagonal = row - col
            anti_diagonal = row + col
            if (col in occupied_cols) or (diagonal in occupied_diagonal) or (anti_diagonal in occupied_anti_diagonal):
                continue
            board[row][col] = "Q"
            occupied_cols.add(col)
            occupied_diagonal.add(diagonal)
            occupied_anti_diagonal.add(anti_diagonal)

            backtrack(row+1)

            board[row][col] = "."
            occupied_cols.remove(col)
            occupied_diagonal.remove(diagonal)
            occupied_anti_diagonal.remove(anti_diagonal)
    backtrack(0)
    return possible_results


print(solve_n_queens(4))
print()
print(solve_n_queens(5))
