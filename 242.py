
'''242. Valid Anagram
Created on 2024-12-18 14:38:39
2024-12-18 14:52:20

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_table: dict[str, int] = {}  #letter: count
        for letter in s:
            seen_table[letter] = seen_table.get(letter, 0) + 1

        for letter in t:
            if seen_table.get(letter, 0) > 0:
                seen_table[letter] -= 1
            else:
                return False

        return True

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
