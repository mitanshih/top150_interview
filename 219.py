
'''219. Contains Duplicate II
Created on 2024-12-19 13:49:32
2024-12-19 14:00:57

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    # Using `set` to record the possible *number* in the range of `k`,
    # space complexity: O(k)
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen_number: set[int] = set()  #record possible value in range of `k`
        for index, number in enumerate(nums):
            if index > k:
                seen_number.remove(nums[index - k - 1])  #sliding window

            if number in seen_number:
                return True    #exist same number in range of `k`

            seen_number.add(number)    #update current number

        return False


class Solution:
    # Using `dictionary` to record the *index* of the latest number,
    # space complexity: O(n)
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen_table: dict[int, int] = {}  #number: index
        for index, number in enumerate(nums):
            if number in seen_table and index - seen_table[number] <= k:
                return True
            #update number in `seen_table` to the latest index
            seen_table[number] = index

        return False


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
