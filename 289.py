
'''289. Game of Life
Created on 2024-12-17 14:08:32
2024-12-17 14:54:25

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    # death: live cell and around live is more than 3 or less than 2
    # live: `live_neighbor` must be 2 or 3 and a live cell,
    # and `live_neighbor` is 3 and it is a dead cell.

    # Consider its cell by add with `live_neighbor` is `live_cell`.
    # While cell is live, `live_cell` is 2 + 1 or 3 + 1,
    # then cell is dead, `live_cell` is 3.
    # Both of the above conditions are live in the next generation.
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for row in range(m):
            for column in range(n):
                live_cell: int = 0    #initialization
                # count `live_neighbor` around and *itself*
                for j in range(row - 1, row + 2):
                    for i in range(column - 1, column + 2):
                        if 0 <= j < m and 0 <= i < n and board[j][i] & 1:
                            live_cell += 1

                    #
                if (live_cell == 3    #whatever dead or live, next is live
                        or (board[row][column] & 1 and live_cell == 4)):
                    board[row][column] |= 2    #use next bit to memorize live
            #
        for j in range(m):
            for i in range(n):
                board[j][i] >>= 1

        # 11: live cell and next generation still live
        # 01:    ...    but dead in next generation
        # 10: dead cell but live in next generation
        # 00: cell always dies


#%%    Main Function
#%%    Main
if __name__ == '__main__':
    pass

#%%
