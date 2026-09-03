class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = len(matrix)
        y = len(matrix[0])
        l = 0
        r = (x * y) - 1

        while l <= r:
            m = int((r+l)//2)
            row = int(m // y)
            col = m - (row * y)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
        