
'''73. Set Matrix Zeroes
Created on 2024-12-13 14:03:10

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero: bool = not all(matrix[0])
        first_column_has_zero: bool = any(matrix[j][0] == 0 for j in range(m))

        #mark `zero` at first row and column of its position,
        # e.g., (5, 2) is zero, mark (5, 0) and (0, 2) as zero.
        for j in range(m):
            for i in range(n):
                if matrix[j][i] == 0:
                    matrix[j][0] = matrix[0][i] = 0

            #
        #check element with its first row and column to assign 0
        for j in range(1, m):
            for i in range(1, n):
                if matrix[0][i] == 0 or matrix[j][0] == 0:
                    matrix[j][i] = 0

            #
        if first_row_has_zero:
            matrix[0][:] = [0] * n

        if first_column_has_zero:
            for j in range(m):
                matrix[j][0] = 0


#%%    Main Function
Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])

#%%    Main
if __name__ == '__main__':
    pass

#%%
