
'''57. Insert Interval
Created on 2024-12-24 16:47:34
2024-12-25 21:19:32

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
#https://leetcode.com/problems/insert-interval/solutions/5975742/video-2-solutions-bonus/
class Solution_reference:
    def insert(self, intervals: list[list[int]], newInterval: list[int]
               ) -> list[list[int]]:
        result: list[list[int]] = []

        for interval in intervals:
            if newInterval[1] < interval[0]:      #overlapping
                result.append(newInterval)
                newInterval = interval    #update `newInterval`
            elif newInterval[0] > interval[1]:    #non-overlapping
                result.append(interval)
            else:                         #adjust `newInterval`
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)        #append the last interval
        return result


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]
               ) -> list[list[int]]:
        result: list[list[int]] = []

        # Insert `newInterval` at the place
        # where `intervals[index][0]` is not smaller than `newInterval[0]`.
        for interval in intervals:
            if interval[1] >= newInterval[0]:
                break

            result.append(interval)

        current: int = len(result)
        length: int = len(intervals)

        # For the *beginning* of `newInterval`,
        # use *minimum* value between `intervals[current]` and `newInterval`.
        if current < length and intervals[current][0] < newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[current][0])

        # Updated/Instead the interval while after adding the `newInterval`.
        while current < length:
            if newInterval[1] < intervals[current][0]:
                break

            current += 1

        # When `current` is 0, prepend `newInterval` to `intervals`.
        # Conversely, for the *end* point of `newInterval`,
        # use the *maximum* value
        # between `intervals[current - 1]` and `newInterval`.
        if current != 0:
            newInterval[1] = max(newInterval[1], intervals[current - 1][1])
        result.append(newInterval)    #append `newInterval` into `result`

        result.extend(intervals[current:])    #extend the rest of `intervals`

        return result


#%%    Main Function
Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1])

#%%    Main
if __name__ == '__main__':
    pass

#%%
