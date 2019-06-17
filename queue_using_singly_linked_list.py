class Node:
    def __init__(self,info,link =None):
        self.info = info
        self.link = link

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
        self.temp_lst = []
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self,item):
        if self.tail == None:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            self.temp_lst.append(item)
        else:
            newNode = Node(item)
            self.tail.link = newNode
            self.tail = newNode
            self.size += 1
            self.temp_lst.append(item)
        return self.temp_lst
    
    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty. Cannot dequeue !')   # Or raise an exception here
        item = self.head.info
        temp_pointer = self.head
        self.head = self.head.link
        temp_pointer.link = None
        self.size -= 1
        return item
        



q = LinkedQueue()
print(q.enqueue(2))
print(q.enqueue(5))
print(q.enqueue(78))
print(q.enqueue(4))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
        
