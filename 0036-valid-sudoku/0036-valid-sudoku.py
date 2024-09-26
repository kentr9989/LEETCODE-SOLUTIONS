class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # {col : <set of value>}
        rows = collections.defaultdict(set) # {row : <set of value>}
        squares = collections.defaultdict(set) #{(r // 3, c // 3 : <set of values>)
        
        for r in range(9):
            for c in range(9):
                if ( board[r][c] in cols[c] or
                     board[r][c] in rows[r] or
                     board[r][c] in squares[(r // 3, c // 3)]):
                    print(cols)
                    print(rows)
                    print(squares)
                    return False
                if board[r][c] != ".":
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r // 3,c // 3)].add(board[r][c])
        return True