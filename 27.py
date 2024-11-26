
'''27. Remove Element
Created on 2024-11-26 13:15:30
2024-11-26 13:46:36

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for index, num in enumerate(nums):
            if num == val:
                while nums and nums[-1] == val:  #element not equal to `val`,
                    nums.pop()                   #to find from the bottom
                # because of O(1) with list.pop() and O(n) with list.pop(0)
                if index >= len(nums):
                    break
                nums[index] = nums.pop()  #last and not equal to `val` element

        return len(nums)


#%%    Main Function
Solution().removeElement([0, 1, 2, 2, 2], 2)

#%%    Main
if __name__ == '__main__':
    pass

#%%
