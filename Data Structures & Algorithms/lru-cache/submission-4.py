class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # store key: nodes
        self.dummyHead = Node(0,0) # dummyHead -> MRU
        self.dummyTail = Node(0,0) # LRU <- dummyTail 
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addMRU(self, node):
        node.next = self.dummyHead.next
        node.prev = self.dummyHead
        self.dummyHead.next.prev = node
        self.dummyHead.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        getNode = self.cache[key]
        # detatch getNode
        self.remove(getNode)
        self.addMRU(getNode)
        
        return getNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.addMRU(node)
        else:
            if len(self.cache) >= self.capacity:
                lruNode = self.dummyTail.prev
                self.remove(lruNode)
                del self.cache[lruNode.key]
            node = Node(key, value)
            self.cache[key] = node
            self.addMRU(node)

            
