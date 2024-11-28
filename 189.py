
'''189. Rotate Array
Created on 2024-11-28 14:03:48
2024-11-28 14:14:04

@author: MilkTea_shih
'''
#TODO: https://leetcode.wang/leetcode-189-Rotate-Array.html  # do solution 3!

#%%    Packages
from collections import deque

#%%    Variable


#%%    Functions
class Solution:
    #Time: O(n)  Space: O(1)
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


class Solution_reverse:
    #Time: O(2n)  Space: O(1)
    def reverse(self, array: list[int], left: int, right: int) -> None:
        while left < right:
            array[left], array[right] = array[right], array[left]

            left += 1
            right -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length: int = len(nums)
        k %= nums_length
        nums.reverse()  #self.reverse(nums, 0, nums_length - 1)  #the same as!
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, nums_length - 1)


class Solution_myself:
    #Time: O(k + n)  Space: O(n)
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_queue: deque[int] = deque(nums)
        temp_queue.rotate(k % len(nums))    #avoid repeated rotations
        for index, num in enumerate(temp_queue):
            nums[index] = num


#%%    Main Function

#%%    Main
if __name__ == '__main__':
    pass

#%%
