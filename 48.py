
'''48. Rotate Image
Created on 2024-12-13 12:43:25
2024-12-13 13:04:11

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for top in range(len(matrix) // 2):    #vertical flip the `matrix`
            matrix[top], matrix[-top - 1] = matrix[-top - 1], matrix[top]

        #transpose the `matrix`
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
