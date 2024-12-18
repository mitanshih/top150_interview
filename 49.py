
'''49. Group Anagrams
Created on 2024-12-18 15:30:04
2024-12-18 15:37:49

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result: dict[tuple[int, ...], list[str]] = {}

        for string in strs:
            count: list[int] = [0] * 26    #26 letters
            for unicode in map(ord, string):    #count each letter
                count[unicode - 97] += 1  #97: ord("a"), unicode of 'a'

            #use encoding of letter count as key to append *anagrams*
            result.setdefault(tuple(count), []).append(string)

        return list(result.values())


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result: dict[tuple[str, ...], list[str]] = {}

        for string in strs:  #use sorted `string` as key to append *anagrams*
            result.setdefault(tuple(sorted(string)), []).append(string)

        return list(result.values())


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
