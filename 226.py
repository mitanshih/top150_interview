
'''226. Invert Binary Tree
Created on 2025-01-09 15:58:02
2025-01-09 16:32:59

@author: MilkTea_shih
'''

#%%    Packages
import collections
from typing import Deque, Optional, Self

#%%    Variable
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Optional[Self] = left
        self.right: Optional[Self] = right

#%%    Functions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_:  #dfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left    #swap

        #recursive the leaves till the end
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class Solution:  #bfs
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        deque: Deque[TreeNode] = collections.deque([root])

        while deque:
            node: TreeNode = deque.popleft()
            node.left, node.right = node.right, node.left    #swap

            #append the leaves
            if node.left is not None:
                deque.append(node.left)
            if node.right is not None:
                deque.append(node.right)

            #
        return root


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
