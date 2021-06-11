class Node:
    def __init__(self,info,link = None):
        self.info = info
        self.link = link

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
    
    def add_item_at_rear(self,item):
        if self.head == None:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode = Node(item)
            self.tail.link = newNode
            self.tail = newNode
            self.size += 1
    
    def add_item_at_front(self,item):
        if self.head == None:
            newNode = Node(item)
            self.head - newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode = Node(item)
            newNode.link = self.head
            self.head = newNode
            self.size += 1

    def add_item_after_a_given_node(self, item, loc):
        if loc == None:                 # If LOC = None, insert as first node
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
    
    def delete_item_from_front(self):
        if self.head == None:
            print("Cannot delete item from empty Linked List")
        else:
            temp_ptr = self.head
            self.head = self.head.link
            temp_ptr.link = None
            self.size -= 1
        return temp_ptr.info

    def traverse(self):
        temp = []
        if self.head == None:
            print("Cannot traverse empty list")
        else:
            self.current_ptr = self.head
            while self.current_ptr != None:
                temp.append(self.current_ptr.info)
                self.current_ptr = self.current_ptr.link
        return temp

    def search_item(self, item):
        location = None
        self.current_ptr = self.head

        while self.current_ptr != None:
            if self.current_ptr.info == item:
                location = self.current_ptr
                return location
        return "Item not available !"


lst = SinglyLinkedList()
lst.add_item_at_rear(34)
lst.add_item_at_rear(6)
lst.add_item_at_rear(78)
lst.add_item_at_rear(2)
lst.add_item_at_rear(367)

        