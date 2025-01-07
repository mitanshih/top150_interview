
'''146. LRU Cache
Created on 2025-01-07 15:24:29
2025-01-07 17:01:41

@author: MilkTea_shih
'''

#%%    Packages
from collections import OrderedDict
from typing import Self

#%%    Variable
class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key: int = key
        self.val: int = val
        self.previous: Self = None  # type: ignore  #point to previous node
        self.next: Self = None      # type: ignore  #point to next node

#%%    Functions
class LRUCache_reference:
    __slots__ = ('cache', 'capacity')

    def __init__(self, capacity: int) -> None:
        self.cache: OrderedDict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        return self.cache.setdefault(    #`pop(key)` and put it back to *top*
            key, self.cache.pop(key)) if key in self.cache else -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value                #update/assign the *key-value*
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:    #ensure the length of `cache`
            self.cache.popitem(last=False)     #clear the Least Rencentlt Used


class LRUCache:
    __slots__ = ('cache', 'capacity', 'oldest_node', 'newest_node')

    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = {}    #mapping `key` to the node
        self.capacity: int = capacity       #maximum of `cache` length

        #dummy node for the oldest and newest `node`
        self.oldest_node: Node = Node(0, 0)
        self.newest_node: Node = Node(0, 0)

        #initialization of the connected of the nodes
        self.oldest_node.next = self.newest_node
        self.newest_node.previous = self.oldest_node

    def __move_to_end(self, node: Node) -> None:
        """Move `node` to the top of the order

        Args:
            node (Node): The node is going to be moving to the top
        """
        self._remove(node)
        self._insert(node)

    def _insert(self, node: Node) -> None:
        """Append the node by connecting `previous` and its from `newest_node`

        Args:
            node (Node): The node is going to be appended
        """
        previous: Node = self.newest_node.previous
        current: Node = self.newest_node

        previous.next = current.previous = node    #add node

        #connect `node` with `current` and `previous`
        node.next = current
        node.previous = previous

    def _remove(self, node: Node) -> None:
        """Delete the node by connecting `left` and `right` beside the `node`

        Args:
            node (Node): The node is going to be deleted
        """
        left, right = node.previous, node.next

        #connect two nodes beside `node`
        left.next = right
        right.previous = left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.__move_to_end(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:    #ensure the length of `cache`
            lru: Node = self.oldest_node.next
            #delete the least recently used node
            self._remove(lru)
            del self.cache[lru.key]    #clear `lru.key` in `cache`


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
