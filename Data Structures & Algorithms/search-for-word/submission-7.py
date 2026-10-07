class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        path = set()
        def backtrack(i, j, indx):
            if indx == len(word):
                return True
            if i < 0 or j<0 or i >= n or j >=m or (i,j) in path or word[indx] != board[i][j]:
                return False
            
            path.add((i,j))
            res = (backtrack(i+1, j, indx+1) or
                backtrack(i, j+1, indx+1) or
                backtrack(i, j-1, indx+1) or
                backtrack(i-1, j, indx+1))
            path.remove((i,j))
            return res
        
        for r in range(n):
            for c in range(m):
                if backtrack(r, c, 0):
                    return True
        return False
        
