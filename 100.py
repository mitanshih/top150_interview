
'''100. Same Tree
Created on 2025-01-08 17:32:00
2025-01-08 18:13:59

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
    def isSameTree(self, p: Optional[TreeNode],
                   q: Optional[TreeNode]
                   ) -> bool:
        if p is None or q is None:    # Any tree reaches the end of the leaf.
            return p == q

        return (    # Check current `TreeNode.val` and recursive to the end.
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

class Solution:  #bfs
    def isSameTree(self, p: Optional[TreeNode],
                   q: Optional[TreeNode]
                   ) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:    # Only one of the parameters is None.
            return False

        p_deque: Deque[TreeNode] = collections.deque([p])
        q_deque: Deque[TreeNode] = collections.deque([q])

        while p_deque and q_deque:
            p_node: TreeNode = p_deque.popleft()
            q_node: TreeNode = q_deque.popleft()

            # Check `TreeNode.val`
            if p_node.val != q_node.val:
                return False

            # Check and append `TreeNode.left`
            if p_node.left is not None and q_node.left is not None:
                p_deque.append(p_node.left)
                q_deque.append(q_node.left)
            elif p_node.left is not None or q_node.left is not None:
                return False

            # Check and append `TreeNode.right`
            if p_node.right is not None and q_node.right is not None:
                p_deque.append(p_node.right)
                q_deque.append(q_node.right)
            elif p_node.right is not None or q_node.right is not None:
                return False

        return not p_deque and not q_deque    #check the rest in deque


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
