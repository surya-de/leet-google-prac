from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        lrow = len(matrix)
        lcol = len(matrix[0])

        for x, row in enumerate(matrix):
            for y, val in enumerate(row):
                if x < lrow - 1 and y < lcol - 1:
                    if matrix[x][y] != matrix[x + 1][y + 1]:
                        return False
        
        return True

if __name__ =='__main__':
    s = Solution()
    #inp = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    inp = [[1,2],[3,1],[4,3]]
    print(s.isToeplitzMatrix(inp))