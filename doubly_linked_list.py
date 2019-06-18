# Author - Anantvir Singh, concept reference:= Data Structures in C by Seymour Lipschutz
class Node:
    def __init__(self,info,forward_link = None,backward_link = None):
        self.FORWARD_LINK = forward_link
        self.info = info
        self.BACKWARD_LINK = backward_link

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr= None
        self.size = 0
        self.temp_list = []          # Note required. Added here to verify if doubly linked list works as expected
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def insert_item_at_head(self,item):
        if self.head == None:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            self.temp_list.append(item)
        else:
            newNode = Node(item)
            newNode.FORWARD_LINK = self.head
            self.head.BACKWARD_LINK = newNode
            self.head = newNode
            newNode.BACKWARD_LINK = None
            self.size += 1
            self.temp_list.append(item)
        return self.temp_list,newNode

    def insert_item_at_tail(self,item):     # similar approach can be followed for insertion at any given location LOC
        if self.tail == None:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            self.temp_list.append(item)
        else:
            newNode = Node(item)
            self.tail.FORWARD_LINK = newNode
            newNode.BACKWARD_LINK = self.tail
            newNode.FORWARD_LINK = None
            self.tail = newNode
            self.size += 1
            self.temp_list.append(item)
        return self.temp_list

    def insert_item_between_nodes(self,item,LOCA,LOCB):     # LOCA = predecessor, LOCB = Successor
        newNode = Node(item)
        newNode.FORWARD_LINK = LOCB
        newNode.BACKWARD_LINK = LOCA
        LOCA.FORWARD_LINK = newNode
        LOCB.BACKWARD_LINK = newNode
        return newNode.info
    
    def traverse_list(self):
        if self.head == None:
            print('Cant traverse. List is Empty !')
        temp_head = self.head
        while self.head != None:
            print(self.head.info)
            self.head = self.head.FORWARD_LINK
        self.head = temp_head


lst = DoublyLinkedList()
print(lst.insert_item_at_head(3))
print(lst.insert_item_at_head(89))
print(lst.insert_item_at_head(98))
print(lst.insert_item_at_head(23))
print(lst.insert_item_at_head(76))
print(lst.insert_item_at_head(14))
lst.traverse_list()
print(lst.insert_item_at_tail(3))
print(lst.insert_item_at_tail(89))
print(lst.insert_item_at_tail(98))
print(lst.insert_item_at_tail(23))
print(lst.insert_item_at_tail(76))
print(lst.insert_item_at_tail(14))
lst.traverse_list()

        