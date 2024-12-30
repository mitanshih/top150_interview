
'''71. Simplify Path
Created on 2024-12-30 16:17:05

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_optimize:
    def simplifyPath(self, path: str) -> str:
        path_list: list[str] = path.split('/')    #separate `path` with '/'
        index: int = 0    # The count for simplified items in list is checked.

        for directory in path_list:
            match directory:
                case '' | '.':    #pass empty/current directory
                    continue
                case '..':        #remove directory to the parent's
                    if index > 0:
                        index -= 1    #move `index` backward to instead

                case _:
                    path_list[index] = directory    #complement `item`
                    index += 1    #move `index` forward with simplified `item`
            #
        return '/' + '/'.join(path_list[:index])  #simplified items in range


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
