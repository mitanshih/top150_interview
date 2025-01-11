
'''
Created on 2025-01-10 13:59:21

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


'''
''.join(_.split('# '))
'''

# [reference]: https://leetcode.com/problems/
# construct-binary-tree-from-preorder-and-inorder-traversal/solutions/
# 5632202/video-2-solutions-with-o-n-2-and-o-n-time
class Solution:
    def buildTree(self, preorder_: list[int], inorder: list[int]
                  ) -> Optional[TreeNode]:
        # Using a hashtable to find the index of `TreeNode.val` with O(1).
        # Without the hashtable, using `list.index(TreeNode.val)` is O(n).
        INORDER_VAL_TO_INDEX: dict[int, int] = {
            value: index for index, value in enumerate(inorder)
        }

        # Optimize `list.pop(0)` in O(n) to `deque.popleft()` in O(1).
        preorder: Deque[int] = collections.deque(preorder_)

        def build(start: int, end: int) -> Optional[TreeNode]:
            """two-pointer to determine the range of the elements in `inorder`

            Args:
                start (int): the beginning index of the subtree
                end (int): the last index of the subtree

            Returns:
                Optional[TreeNode]: the node, `root` of tree/subtree
            """
            if start > end:    #out of the range
                return None

            root: TreeNode = TreeNode(preorder.popleft())    #build `TreeNode`
            middle: int = INORDER_VAL_TO_INDEX[root.val]     #index of `root`

            # Recursive except `middle` because it is the root of the subtree.
            root.left = build(start, middle - 1)
            root.right = build(middle + 1, end)

            return root

        return build(0, len(preorder_) - 1)    #recursive the whole `preorder`


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
