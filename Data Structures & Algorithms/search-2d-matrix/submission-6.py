class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = (m*n)-1

        while l <= r:
            mid = (l+r)//2
            # split into rows and cols (coords)
            row = mid // n
            col = mid - (row*n)
            curr = matrix[row][col]

            if curr == target:
                return True
            
            elif curr < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False