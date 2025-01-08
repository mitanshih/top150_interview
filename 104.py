
'''104. Maximum Depth of Binary Tree
Created on 2025-01-08 16:15:51

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

class Solution_reference:  #dfs
    #Time: O(n)
    #Space: O(h), `h` is the max height of `root`
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if root is None \
            else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:  #bfs
    #Time: O(n)
    #Space: O(w), `w` is the max width of `root`
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        result: int = 0
        deque: Deque[TreeNode] = collections.deque([root])
        while deque:
            # Append the leaves under `node`.
            for _ in range(len(deque)):
                node: TreeNode = deque.popleft()
                if node.left is not None:
                    deque.append(node.left)
                if node.right is not None:
                    deque.append(node.right)

            result += 1    #move to the next level

        return result


#%%    Main Function

#%%    Main
if __name__ == '__main__':
    pass

#%%
