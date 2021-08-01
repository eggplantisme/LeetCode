class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row = [board[i][k] for k in range(9) if board[i][k] != '.' and k != j]
                    col = [board[k][j] for k in range(9) if board[k][j] != '.' and k != i]
                    square = []
                    for p in range(i // 3 * 3, i // 3 * 3 + 3):
                        for q in range(j // 3 * 3, j // 3 * 3 + 3):
                            if board[p][q] != '.' and p != i and q != j:
                                square.append(board[p][q])
                    if board[i][j] in row or board[i][j] in col or board[i][j] in square:
                        return False
        return True


print(Solution().isValidSudoku(
    [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]))