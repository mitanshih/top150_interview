
'''383. Ransom Note
Created on 2024-12-18 12:47:59
2024-12-18 12:55:56

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_table: dict[str, int] = {}
        for letter in magazine:
            letter_table[letter] = letter_table.get(letter, 0) + 1

        for letter in ransomNote:
            if letter_table.get(letter, 0) > 0:
                letter_table[letter] -= 1
            else:
                return False
        return True

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
