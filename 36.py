
'''36. Valid Sudoku
Created on 2024-12-10 12:35:33
2024-12-10 15:29:53

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        ''' bitmask for the `number`, such as '9' -> `8` -> 00001000
            8: 00001000
            2: 00000010

            8 & 2 = 00000000 = 0 -> False
            8 |= 2 = 00001010 = 10

            10 & 8 = 00001000 = 8 -> True
        '''
        rows: list[int] = [0] * 9
        columns: list[int] = [0] * 9
        boxes: list[int] = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num: int = ord(board[i][j]) - ord('1')  #convert string to 0-8
                mask: int = 1 << num                    #bitmask for number
                box_index: int = (i // 3) * 3 + (j // 3)

                # Check the number is already set in the row, column, or box.
                if any(
                    ((rows[i] & mask),
                     (columns[j] & mask),
                     (boxes[box_index] & mask),
                     )
                ):
                    return False

                # Mark the number in the row, column, and box
                rows[i] |= mask
                columns[j] |= mask
                boxes[box_index] |= mask

        return True    #all pass!


class Solution:
    def flatten_list(self, nested_list: list) -> list[str]:
        flat_list: list[str] = []

        def flatten_recursive(x: list) -> None:
            for item in x:
                if isinstance(item, list):
                    flatten_recursive(item)
                else:
                    flat_list.append(item)
            #

        flatten_recursive(nested_list)
        return flat_list

    def is_valid(self, x: list) -> bool:
        flat_x: list[str] = list(
            filter(lambda x: x != '.', self.flatten_list(x)))

        return len(set(flat_x)) == len(flat_x)  #*True*: there is no duplicate

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #       `board`      => `transposed_board`
        #     [[0, 1, 2],          [[0, 3, 6],
        #      [3, 4, 5],    =>     [1, 4, 7],
        #      [6, 7, 8]]           [2, 5, 8]]
        transposed_board: list[list[str]] = list(map(list, zip(*board)))

        # [[0, 1, 2],
        #  [3, 4, 5],
        #  [6, 7, 8]]
        # The first `section` checks each row from 0-2 and 0, 1, 2 area.
        for section in range(0, 9, 3):  #section: 0, 3, 6
            for area in range(section, section + 3):  #0~2, 3~5, 6~8
                index: int = (area * 3) % 9
                if not all(
                    (self.is_valid(board[area]),  #check row
                     self.is_valid(transposed_board[area]),  #check column
                     self.is_valid([row[index:index + 3]  #check `area`
                                    for row in board[section:section + 3]]),
                     )
                ):
                    return False

        return True


#%%    Main Function
test = [[".", ".", ".", ".", ".", ".", "5", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["9", "3", ".", ".", "2", ".", "4", ".", "."],
        [".", ".", "7", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "3", "4", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "."],
        [".", ".", ".", ".", ".", "5", "2", ".", "."]]

Solution().isValidSudoku(test)

#%%    Main
if __name__ == '__main__':
    pass

#%%
