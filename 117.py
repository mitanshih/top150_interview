
'''117. Populating Next Right Pointers in Each Node II
Created on 2025-01-13 15:25:41
2025-01-13 17:48:18

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional, Self

#%%    Variable
class Node:
    def __init__(self, val: int = 0,
                 left: Optional[Self] = None,
                 right: Optional[Self] = None,
                 next: Optional[Self] = None
                 ) -> None:
        self.val: int = val
        self.left: Optional[Self] = left
        self.right: Optional[Self] = right
        self.next: Optional[Self] = next


#%%    Functions
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, 
                 left: Optional[Self] = None, 
                 right: Optional[Self] = None, 
                 next: Optional[Self] = None
                 ) -> None:
        self.val: int = val
        self.left: Optional[Self] = left
        self.right: Optional[Self] = right
        self.next: Optional[Self] = next
"""

class Solution_reference:  #bfs
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None

        dummy_node: Node = Node()    #dummy for connecting the other nodes

        current: Optional[Node] = root
        while current is not None:
            temp: Node = dummy_node

            scanner: Optional[Node] = current
            while scanner is not None:    #connect all the nodes in same level
                if scanner.left is not None:
                    temp.next = scanner.left
                    temp = temp.next

                if scanner.right is not None:
                    temp.next = scanner.right
                    temp = temp.next

                scanner = scanner.next

            current = dummy_node.next    #move to leftmost node of next level
            dummy_node.next = None    #initialization

        return root


class Solution:  #dfs
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None

        scanner: Optional[Node] = root.next
        while scanner is not None:    #scan the closest node for connected
            if scanner.left is not None:
                scanner = scanner.left
                break
            elif scanner.right is not None:
                scanner = scanner.right
                break

            scanner = scanner.next

        #connect `root.right.next` to `scanner` first if `root.right` exists
        # Because the right node of the subtree is connected
        # to the next left node of another subtree.
        if root.right is not None:
            root.right.next = scanner

        #connect `root.left.next` to `root.right` depends on its right exists
        # or connect to `scanner`
        if root.left is not None:
            root.left.next = root.right if root.right is not None else scanner

        #recursive to the end of `root`, connect the right node at first
        self.connect(root.right)
        self.connect(root.left)

        return root


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
