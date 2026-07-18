class Solution:

    def solve(self, col, board, n):
        if col == n:
            return 1
        
        count = 0

        for row in range(n):

            if self.isSafe(row, col, board, n):

                board[row] = board[row][: col] + "Q" + board[row][col+1 :]
                count += self.solve(col+1, board, n)
                board[row] = board[row][: col] + "." + board[row][col+1 :]

        return count
    
    def isSafe(self, row, col, board, n):

        duprow = row
        dupcol = col
        while row>=0 and col>=0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row = duprow
        col = dupcol
        while col>=0:
            if board[row][col] == "Q":
                return False
            col -= 1

        row = duprow
        col = dupcol
        while row<n and col>=0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1

        return True
    
    def totalNQueens(self, n):

        board = ["." * n for _ in range(n)]
        return self.solve(0, board, n)