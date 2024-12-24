
'''57. Insert Interval
Created on 2024-12-24 16:47:34
2024-12-25 21:19:32

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]
               ) -> list[list[int]]:
        if intervals == []:    #edge case
            return [newInterval]
        result: list[list[int]] = []

        for interval in intervals:    #find the place to insert
            if interval[1] >= newInterval[0]:
                break
            result.append(interval)

        current: int = len(result)
        limit: int = len(intervals)

        #check overlapping with the front of `newInterval`
        if current < limit and intervals[current][0] < newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[current][0])

        while current < limit:    #the range instead by `newInterval`
            if intervals[current][0] > newInterval[1]:
                break
            current += 1

        if current == 0:    # `newInterval` is the first interval.
            result.append(newInterval)
        else:
            result.append([newInterval[0],    #the end point of final interval
                           max(intervals[current - 1][1], newInterval[1])])
        result.extend(intervals[current:])    #extend the rest of `intervals`

        return result


#%%    Main Function
Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1])

#%%    Main
if __name__ == '__main__':
    pass

#%%
