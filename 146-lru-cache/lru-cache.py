class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     #key is mapped to a node
        
        self.left = Node(0,0)  #left is least recently used
        self.right = Node(0,0)  #right is most recent
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next , nxt.prev = nxt, prev
        # node.prev.next = node.next
        # node.next.prev = node.prev

    #insert in the right position
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
        # prev, nxt = self.right.prev, self.right
        # prev.next = prev.next = node
        # node.next = node.prev = node
        # node.next, node.prev = nxt, prev
        # node.next = self.right.prev
        # node.prev = self.left.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            #now before returning i will have to make the one accessed key to the left(LRU)
            self.remove(self.cache[key])   #we remove and add again so that its in the right now
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        #if key is already existing then we need to update the value basically remove and insert 
        #ELSE JUST INSERT
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        #now we check for the capacity
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)