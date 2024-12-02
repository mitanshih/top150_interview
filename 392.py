
'''392. Is Subsequence
Created on 2024-12-02 17:00:36
2024-12-02 17:35:50

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < 2:    #eage case
            return s == t
        s_length, t_limit = len(s), len(t) - 1

        s_index = t_index = 0    # two-pointer
        while s_index < s_length:
            if s[s_index] == t[t_index]:
                s_index += 1

            t_index += 1
            if t_index > t_limit:
                break
        else:
            return True
        return s_index == s_length    # No matching the `s` in `t`?


#%%    Main Function
Solution().isSubsequence('abc', 'ahbgdc')

#%%    Main
if __name__ == '__main__':
    pass

#%%
