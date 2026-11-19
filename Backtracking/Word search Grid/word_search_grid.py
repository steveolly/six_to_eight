def word_exists(board, word):
    if not word:
        return False
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])

    def backtrack(row, col, index):
        if index == len(word):
            return True

        if (row < 0) or (row >= rows) or (col < 0) or (col >= cols) or (board[row][col] != word[index]):
            return False

        orignal, board[row][col] = board[row][col], "#"

        found = (
            backtrack(row+1, col, index+1)
            or backtrack(row, col+1, index+1)
            or backtrack(row-1, col, index+1)
            or backtrack(row, col-1, index+1)
        )

        board[row][col] = orignal

        return found

    for r in range(len(board)):
        for c in range(len(board[0])):
            if backtrack(r, c, 0):
                return True
    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
print(word_exists(board, "ABCCED"))
print(word_exists(board, "ABCB"))
print(word_exists(board, "SFBCESEED"))
print(word_exists(board, "SFCSEE"))
