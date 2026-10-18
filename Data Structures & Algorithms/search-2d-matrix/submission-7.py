class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = (ROWS * COLS) - 1

        while l <= r:
            m = (l+r)//2
            row = m // COLS
            col = m - (row * COLS)

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1
        
        return False