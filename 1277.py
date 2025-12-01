#contar quantas submatrizes quadradas contêm apenas 1s

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        total_squares = 0
        
        for r in range(rows):
            for c in range(cols):
                
                if matrix[r][c] == 1:
                    
                    if r == 0 or c == 0:
                        pass
                    
                    else:
                        matrix[r][c] = min(
                            matrix[r - 1][c],      # superior
                            matrix[r][c - 1],      # esquerdo
                            matrix[r - 1][c - 1]   # diagonal
                        ) + 1
                
                total_squares += matrix[r][c]

        return total_squares