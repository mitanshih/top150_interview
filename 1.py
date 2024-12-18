
'''1. Two Sum
Created on 2024-12-18 16:30:40
2024-12-18 16:37:24

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_table: dict[int, int] = {}  #number: index

        for index, number in enumerate(nums):
            if (target - number) in seen_table:
                break
            seen_table[number] = index

        return [seen_table[target - number], index]

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
