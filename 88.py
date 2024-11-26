
'''88. Merge Sorted Array
Created on 2024-11-25 13:33:57
2024-11-25 14:07:16

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp: list[int] = nums1.copy()    #avoid shadow copy in 1-D array

        i = j = k = 0    #`i` and `j` is the index for `temp` and `nums2`
        #`k` is the current index for `nums` to instead value.
        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1

        for num in nums2[j:n] if j < n else temp[i:m]:
            nums1[k] = num
            k += 1


#%%    Main Function
Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

#%%    Main
if __name__ == '__main__':
    pass

#%%
