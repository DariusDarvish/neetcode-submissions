class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.nxt=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.node_index={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.nxt=self.tail
        self.tail.prev=self.head

    def add(self,node) -> None:
        next_node=self.head.nxt
        node.nxt=next_node
        node.prev=self.head
        next_node.prev=node
        self.head.nxt=node
    
    def remove(self,node) -> None:
        previous_node=node.prev
        next_node=node.nxt
        next_node.prev=previous_node
        previous_node.nxt=next_node


    def get(self, key: int) -> int:
        if key not in self.node_index:
            return -1
        node=self.node_index[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_index:
            self.node_index[key].val=value
            self.get(key)
            return None
        if self.capacity==len(self.node_index):
            node_to_remove=self.tail.prev
            self.remove(node_to_remove)
            del self.node_index[node_to_remove.key]

        node=Node(key,value)
        self.add(node)
        self.node_index[key]=node

        
