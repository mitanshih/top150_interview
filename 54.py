
'''54. Spiral Matrix
Created on 2024-12-10 16:48:07
2024-12-10 17:39:06

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []

        top = left = 0
        bottom: int = len(matrix) - 1
        right: int = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # top: from `left` to `right`
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # right: from `top` to `bottom`
            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1

            if top <= bottom:
                # bottom: from `right` to `left`
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # left: from `bottom` to `top`
                for j in range(bottom, top - 1, -1):
                    result.append(matrix[j][left])
                left += 1

        return result


class Solution_seen:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y = 0, 0    #initialize position at the upper left, (0, 0)
        dx, dy = 1, 0    #first move the `x`-direction with *positive*
        result: list[int] = []

        for _ in range(rows * cols):
            result.append(matrix[y][x])    #step-by-step
            matrix[y][x] = 1000    #because of `-100 <= matrix[i][j] <= 100`

            if ((not 0 <= x + dx < cols or not 0 <= y + dy < rows)
                    or matrix[y + dy][x + dx] == 1000):    # 1000: has seen
                dx, dy = -dy, dx    #change the direction of movement

            x += dx
            y += dy

        return result


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
