
'''452. Minimum Number of Arrows to Burst Balloons
Created on 2024-12-30 13:22:48
2024-12-30 13:54:15

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])    #sort `point` with its end point

        #slice the first element in `points`, and take its end point as `end`
        (_, arrow_shot_end), *points = points
        result: int = 1  #1 shot in constraints of `1 <= points.length <= 105`

        for interval in points:
            if interval[0] > arrow_shot_end:    # Current point is over `end`.
                arrow_shot_end = interval[1]    #new point of `end`
                result += 1

        return result


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])    #sort `point` with its start point

        #slice the first element in `points`, and take its end point as `end`
        (_, arrow_shot_end), *points = points
        result: int = 1  #1 shot in constraints of `1 <= points.length <= 105`

        for interval in points:
            if interval[0] > arrow_shot_end:    # Current point is over `end`.
                arrow_shot_end = interval[1]    #new point of `end`
                result += 1
            else:    #let `arrow_shot_end` close to `start` point
                arrow_shot_end = min(arrow_shot_end, interval[1])

        return result

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
