
'''80. Remove Duplicates from Sorted Array II
Created on 2024-11-26 21:32:18
2024-11-26 22:05:25

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        unique_number_index: int = 2
        for num in nums[2:]:
            if num != nums[unique_number_index - 2]:
                nums[unique_number_index] = num
                unique_number_index += 1

        return unique_number_index


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        has_duplicate: bool = False

        unique_number_index: int = 0
        for num in nums[1:]:
            if num == nums[unique_number_index]:
                if has_duplicate:    #duplication more than 2 times
                    continue         #[1, 1, *1*, (*1*, ...)]
                has_duplicate = True    #first duplication: [1, *1*]
            else:
                # In non-decreasing order,
                # if the num[i] is not equal to num[i + 1],
                # it must smaller than num[i + 1].
                has_duplicate = False

            unique_number_index += 1
            nums[unique_number_index] = num

        return unique_number_index + 1


#%%    Main Function
Solution().removeDuplicates([1, 1, 1, 2, 2, 3])

#%%    Main
if __name__ == '__main__':
    pass

#%%
