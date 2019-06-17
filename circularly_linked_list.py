# Author - Anantvir Singh, concept reference:= Data Structures in C by Seymour Lipschutz
class Node:
    def __init__(self,info,link = None):
        self.info = info
        self.link = link

class CircularLinkedQueue:
    def __init__(self):
        self.head = None            # Although explicit reference to head not required as it can be acced via tail.link but I maintain it for clarity and ease of understanding
        self.tail = None
        self.current_ptr = None
        self.size = 0
        self.temp_list = []         # not required. Added just to test if this linked list works as expected

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def enqueue(self,item):
        if self.size == 0:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.tail.link = self.head
            self.size += 1
            self.temp_list.append(item)
        else:
            newNode = Node(item)
            self.tail.link = newNode
            self.tail = newNode
            newNode.link = self.head
            self.size += 1
            self.temp_list.append(item)
        return self.temp_list
    
    def dequeue(self):
        if self.size == 0:
            print('Queue is Empty !')
        item = self.head.info
        temp_pointer = self.head
        self.head = self.head.link
        temp_pointer.link = None
        self.tail.link = self.head
        return item

q = CircularLinkedQueue()
print(q.enqueue(5))
print(q.enqueue(9))
print(q.enqueue(2))
print(q.enqueue(6))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

                