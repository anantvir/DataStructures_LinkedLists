class Node:
    def __init__(self,info,link= None):
        self.info = info
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
    
    def add_element_at_rear(self,element):
        if self.head == None:
            newNode = Node(element)
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode = Node(element)
            self.tail.link = newNode
            self.tail = newNode
            self.size += 1
        return newNode
    
    def traverse_linked_list(self):
        temp_list =[]
        if self.current_ptr == None:
            self.current_ptr = self.head
        while self.current_ptr != None:
            temp_list.append(self.current_ptr.info)
            self.current_ptr = self.current_ptr.link
        return temp_list


    
lst = LinkedList()
lst.add_element_at_rear(2)
lst.add_element_at_rear(5)
lst.add_element_at_rear(8)

temp = lst.traverse_linked_list()
for x in range(len(temp)):
    print(temp[x])
