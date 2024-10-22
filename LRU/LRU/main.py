from abc import ABC, abstractmethod

class Node:
    """
    Node in a doubly linked list
    SOLID: 
    1. Single Responsibility: Responsible only for representing a single node in the linked list.
    """
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class Cache:
    """
    Abrstract class for cache
    SOLID: 
    1. Single Responsibility: Responsible only for defining the interface for a cache.
    2. Open/Closed : The Cache abstract class allows you to implement different cache strategies without modifying the existing LRUCache.
                     For example, you could create a FifoCache or another type of cache by extending the Cache interface.
    3. Liskov Substitution: The LRUCache class can be used in place of the Cache class^.
    4. Interface Segregation: Clients using this interface do not have to implement or depend on methods that are irrelevant to their needs.
    """
    @abstractmethod
    def get(self, key: int) -> int:
        pass

    @abstractmethod
    def put(self, key: int, value: int) -> None:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

class LRU(Cache):
    """
    Least Recently Used (LRU) cache implementation
    SOLID: 
    1. Single Responsibility: Responsible only for implementing the LRU cache strategy.
    2. Dependency Inversion: The LRUCache class depends on the Cache abstract class, which allows it to be used in place of the Cache interface.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current_size = 0

    def _remove(self, node: Node) -> None:
        """
        Private method to remove a node from the linked list
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node  
        self.current_size -= 1


    def _add_to_front(self, node: Node) -> None:
        """
        Private method to add a node to the head of the linked list
        """
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        self.current_size += 1


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add_to_front(node)

        else:
            if self.current_size >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def size(self) -> int:
        return self.current_size


if __name__ == "__main__":
    lru_cache = LRU(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))  # Returns 1
    print(lru_cache.size())   # Returns 2 (size of the cache)
    lru_cache.put(3, 3)      # Evicts key 2
    print(lru_cache.size())   # Returns 2 (size of the cache)
    print(lru_cache.get(2))  # Returns -1 (not found)
    lru_cache.put(4, 4)      # Evicts key 1
    print(lru_cache.size())   # Returns 2 (size of the cache)
    print(lru_cache.get(1))  # Returns -1 (not found)
    print(lru_cache.get(3))  # Returns 3
    print(lru_cache.get(4))  # Returns 4








"""
^
LSP:

def use_cache(cache: Cache):
    cache.put(1, 100)
    print(cache.get(1))
    print(cache.size())

# Now we can pass any cache that implements Cache
lru_cache = LRUCache(2)
use_cache(lru_cache)  # Works fine

# If we had another implementation, say FIFOCache
class FIFOCache(Cache):
    def get(self, key: int) -> int:
        pass  # Implementation goes here

    def put(self, key: int, value: int) -> None:
        pass  # Implementation goes here
    
    def size(self) -> int:
        pass  # Implementation goes here

fifo_cache = FIFOCache()
use_cache(fifo_cache)  # This would also work fine if FIFOCache is correctly implemented


"""    