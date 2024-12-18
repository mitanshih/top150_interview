
'''205. Isomorphic Strings
Created on 2024-12-18 13:19:49
2024-12-18 13:38:54

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped_set: set[tuple[str, str]] = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_table: dict[str, str] = {}
        seen_letter: set[str] = set()
        for index in range(len(s)):
            if s[index] in mapping_table:
                if mapping_table[s[index]] != t[index]:
                    return False    #wrong mapping from `s[index] -> t[index]`
            else:
                if t[index] in seen_letter:
                    return False    #`t[index]` not mapping to same `s[index]`
                mapping_table[s[index]] = t[index]
                seen_letter.add(t[index])

        return True

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
