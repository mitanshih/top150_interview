
'''169. Majority Element
Created on 2024-11-27 13:56:58

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]    #middle position in `nums`


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num_table: dict[int, int] = {}
        for num in nums:
            num_table[num] = num_table.get(num, 0) + 1

        return sorted(num_table.items(), key=lambda x: x[1]).pop()[0]

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
