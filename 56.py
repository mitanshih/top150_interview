
'''56. Merge Intervals
Created on 2024-12-24 15:45:01

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    #Time: O(n * log(n) + n)
    #Space: O(1)    #replace the non-overlapping interval in-place
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])    #sorted with the first element
        k: int = 0    #non-overlapping interval count

        for interval in intervals[1:]:
            if interval[0] <= intervals[k][1]:    #overlapping intervals
                intervals[k][1] = max(intervals[k][1], interval[1])
            else:
                k += 1    #non-overlapping intervals
                intervals[k] = interval    #replace in-place

        return intervals[:k + 1]


class Solution:
    #Time: O(n * log(n) + n)
    #Space: O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])    #sorted with the first element
        result: list[list[int]] = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:    #overlapping intervals
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)        #non-overlapping intervals

        return result


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
