class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # maps key -> Node
        self.capacity = capacity
        self.left_sentinel, self.right_sentinel = Node(), Node()
        self.left_sentinel.next, self.right_sentinel.prev = self.right_sentinel, self.left_sentinel

    def _append(self, node: Node) -> None:
        node.prev, node.next = self.right_sentinel.prev, self.right_sentinel
        self.right_sentinel.prev.next = node
        self.right_sentinel.prev = node

    def _remove(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _popleft(self) -> int:
        lru_node = self.left_sentinel.next
        self._remove(lru_node)
        return lru_node.key

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node is None:
            return -1
        # move key to MRU position
        self._remove(node)
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._append(node)
        else:
            if len(self.cache) == self.capacity:
                # remove LRU key
                self.cache.pop(self._popleft())
            node = Node(key, value)
            self._append(node)
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
