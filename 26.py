
'''26. Remove Duplicates from Sorted Array
Created on 2024-11-26 17:45:43

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_number_index: int = 0
        for num in nums:
            if num > nums[unique_number_index]:
                unique_number_index += 1    #pre-add for first unique element
                nums[unique_number_index] = num

        return unique_number_index + 1    #at least 1 unique number

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
