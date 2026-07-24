class Solution:

    def solve(self,col,board,ans,leftrow,upperDiagonal,lowerDiagnal,n):
        if col == n:
            ans.append(board[:])
            return
        
        for row in range(n):
            if (
                leftrow[row] == 0
                and lowerDiagnal[row + col] == 0
                and upperDiagonal[(n-1) + (col-row)] == 0
            ):
                board[row] = board[row][: col] + "Q" + board[row][col+1 :]
                leftrow[row] = 1
                lowerDiagnal[row + col] = 1
                upperDiagonal[(n-1) + (col-row)] = 1

                self.solve(col+1, board, ans, leftrow, upperDiagonal, lowerDiagnal, n)

                board[row] = board[row][: col] + "." + board[row][col+1 :]
                leftrow[row] = 0
                lowerDiagnal[row + col] = 0
                upperDiagonal[(n-1) + (col-row)] = 0

    def solveNQueens(self, n):
        ans = []
        board = ["."*n for _ in range]
        leftrow = [0] * n
        lowerDiagnal = [0] * (2 * n - 1)
        upperDiagonal = [0] * (2 * n - 1)

        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagnal, n)
        return ans