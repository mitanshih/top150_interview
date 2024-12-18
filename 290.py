
'''290. Word Pattern
Created on 2024-12-18 14:20:52

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words: list[str] = s.split(' ')    #separate word by *space*
        if len(pattern) != len(s_words):
            return False
        mapping_table: set[tuple[str, str]] = set(zip(pattern, s_words))
        return len(mapping_table) == len(set(pattern)) == len(set(s_words))

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
