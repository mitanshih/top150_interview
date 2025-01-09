
'''101. Symmetric Tree
Created on 2025-01-09 17:04:16
2025-01-09 17:49:06

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

class Solution:  #dfs
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:     #pass both leaves are None
                return True
            elif left is None or right is None:    #only one leaf in this node
                return False

            return (left.val == right.val    #verify two nodes
                    and dfs(left.left, right.right)     #outside mirror
                    and dfs(left.right, right.left))    #inside mirror

        return dfs(root.left, root.right)    #recursive to the end and check


class Solution_:  #bfs
    def isSymmetric(self, root: TreeNode) -> bool:
        left_deque: Deque[Optional[TreeNode]] = collections.deque([root])
        right_deque: Deque[Optional[TreeNode]] = collections.deque([root])

        while left_deque and right_deque:
            left: Optional[TreeNode] = left_deque.popleft()
            right: Optional[TreeNode] = right_deque.popleft()

            if left is None and right is None:    #pass both leaves are None
                continue
            elif left is None or right is None or (left.val != right.val):
                return False

            #append the leaf in a different order in `left` and `right`
            left_deque.append(left.left)
            left_deque.append(left.right)
            right_deque.append(right.right)
            right_deque.append(right.left)

        return True


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
