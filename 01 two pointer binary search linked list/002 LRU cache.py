class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None

    
    def add_node(self, node):

        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        cur_node = self.dict[key]
        # because you get it, that means this node get used. we need to replace this node to the tail
        self.remove_node(cur_node)
        self.add_node(cur_node)

        return cur_node.value

    def put(self, key: int, value: int) -> None:

        if key in self.dict:
            self.remove_node(self.dict[key])

        new_node = ListNode(key, value)
        self.dict[key] = new_node
        self.add_node(new_node)

        if len(self.dict) > self.capacity:
            to_delete_node = self.head.next
            self.remove_node(to_delete_node)
            del self.dict[to_delete_node.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)