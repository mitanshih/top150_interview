
'''106. Construct Binary Tree from Inorder and Postorder Traversal
Created on 2025-01-13 13:09:16
2025-01-13 13:35:18

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional, Self

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

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]
                  ) -> Optional[TreeNode]:
        # Using a hashtable to find the index of `TreeNode.val` with O(1).
        # Without the hashtable, using `list.index(TreeNode.val)` is O(n).
        INORDER_VAL_TO_INDEX: dict[int, int] = {
            value: index for index, value in enumerate(inorder)
        }

        def build(start: int, end: int) -> Optional[TreeNode]:
            """two-pointer to determine the range of the elements in `inorder`

            Args:
                start (int): the beginning index of the subtree
                end (int): the last index of the subtree

            Returns:
                Optional[TreeNode]: the node, `root` of tree/subtree
            """
            if start > end:
                return None

            root: TreeNode = TreeNode(postorder.pop())      #build `TreeNode`
            middle: int = INORDER_VAL_TO_INDEX[root.val]    #index of `root`

            # Recursive except `middle` because it is the root of the subtree.
            root.right = build(middle + 1, end)
            root.left = build(start, middle - 1)

            return root

        return build(0, len(postorder) - 1)


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
