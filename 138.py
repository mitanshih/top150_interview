
'''138. Copy List with Random Pointer
Created on 2025-01-02 22:44:19

@author: MilkTea_shih
'''

#%%    Packages
from typing import Self, Optional

#%%    Variable
class Node:
    def __init__(self, x: int,
                 next: Optional[Self] = None,
                 random: Optional[Self] = None
                 ) -> None:
        self.val: int = int(x)
        self.next: Optional[Self] = next
        self.random: Optional[Self] = random


#%%    Functions
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution_space_in_1:
    # Time: O(n + n + n)
    # Space: O(1)    #copied the node and sperate the result in `head`
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        if head is None:    #edge case
            return None

        current: Optional[Node] = head
        #traverse `head` and copy `current` node after `current`
        while current is not None:
            copied_node: Node = Node(current.val, current.next)    #copy node
            current.next = copied_node    #put `copied_node` after `current`

            current = copied_node.next    #go next node in origianl `head`

        current = head
        #assign `Node.random` from original to copied node
        while current is not None and current.next is not None:
            if current.random is not None:
                #current.random: point to the original node
                #current.random.next: point to the copied after origianl node
                current.next.random = current.random.next

            current = current.next.next    #go next node in origianl `head`

        current = head
        # The next node in head is used as beginning node for copied.
        copied_current: Optional[Node] = head.next
        result_head: Optional[Node] = copied_current    #record head of result
        while current is not None and current.next is not None:
            # Restore the original linked list before `copied_node` was added.
            current.next = current.next.next  #go next node in origianl `head`

            # Sperate the copied node as copied linked list from the original.
            if copied_current is not None and copied_current.next is not None:
                copied_current.next = copied_current.next.next

            # Go next node respectively.
                copied_current = copied_current.next
            current = current.next
            #

        return result_head


class Solution:
    # Time: O(n + n)
    # Space: O(n)    #for mapping the old node to the new node
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        result: dict[Optional[Node], Node] = {
            #**memory address**
            #old_node: new_node
        }

        current: Optional[Node] = head
        #traverse `head` and add a mapping from original to new copied node
        while current is not None:
            result[current] = Node(current.val)

            current = current.next

        current = head
        #mapping `Node.next` and `Node.random` from original to new node
        while current is not None:
            #The attributes of the new node are gotten from the old node.
            result[current].next = result.get(current.next)
            result[current].random = result.get(current.random)

            current = current.next

        return result.get(head)


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
