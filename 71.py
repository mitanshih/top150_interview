
'''71. Simplify Path
Created on 2024-12-30 16:17:05

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path_list: list[str] = []

        for item in path.split('/'):    #separate `path` with '/'
            if item == '..':    #remove directory legally
                simplified_path_list.pop() if simplified_path_list else 0
            elif item and item != '.':    #directory without current or empty
                simplified_path_list.append(item)
            #else:
                #pass the current/empty directory

        return '/' + '/'.join(simplified_path_list)

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
