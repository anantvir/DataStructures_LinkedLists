# Author - Anantvir Singh, reference:= Data Structures in C by Seymour Lipschutz
class Node:
    def __init__(self,info,link= None):
        self.info = info
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None         # maintain a current pointer
        self.size = 0
    
    def add_item_at_rear(self,item):
        if self.head == None:           # list initially empty ?
            newNode = Node(item)
            self.head = newNode         
            self.tail = newNode
            self.size += 1
        else:
            newNode = Node(item)
            self.tail.link = newNode
            self.tail = newNode
            self.size += 1
        return newNode
    
    def add_item_at_front(self,item):
        if self.head == None:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.current_ptr = newNode
            self.size += 1
        else:
            newNode = Node(item)
            newNode.link = self.head
            self.head = newNode
            self.size += 1
        return newNode
    
    def add_item_after_a_given_node(self,item,loc):      # loc = location of new given node
        if loc == None:
            newNode = Node(item)
            newNode.link = self.head
            self.head = newNode
        else:
            newNode = Node(item)
            newNode.link = loc.link
            loc.link = newNode
        return newNode
    
    def delete_item_from_front(self):
        if self.head == None:
            print('Cant delete from front. List is empty !')    # better raise exception here to avoid runtime errors
        temp_pointer = self.head
        self.head = self.head.link
        temp_pointer.link = None
        return temp_pointer.info


    def traverse_linked_list(self):
        temp_list =[]
        if self.current_ptr == None:
            self.current_ptr = self.head                #initialize current pointer to start/head of list
        while self.current_ptr != None:                 # while last item with link = Null/None is not reached
            temp_list.append(self.current_ptr.info)     #process the item
            self.current_ptr = self.current_ptr.link    #increment the pointer
        return temp_list

    def search_item(self,item):                         # Assume list is unsorted
        location = None
        if self.current_ptr == None:
            self.current_ptr = self.head
        while self.current_ptr != None:
            if self.current_ptr.info == item:
                location = self.current_ptr
                self.current_ptr = self.current_ptr.link
            else:
                self.current_ptr = self.current_ptr.link
        
        if location == None:
            print('Cannot find the item !')         # or raise any exception
        return location
           
lst = LinkedList()
lst.add_item_at_rear(2)
lst.add_item_at_rear(5)
lst.add_item_at_rear(8)

