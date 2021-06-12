class Node:
    def __init__(self, data, forward_link = None, backward_link = None):
        self.data = data
        self.forward_link = forward_link
        self.backward_link = backward_link

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
        self.temp_list = []

    def isEmpty(self):
        return self.size == 0

    def insert_at_head(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            self.temp_list.append(newNode.data)
        else:
            newNode = Node(data)
            newNode.forward_link = self.head
            self.head.backward_link = newNode
            self.head = newNode
            self.size += 1 
            self.temp_list.append(newNode.data)
        return self.temp_list, newNode     

    def insert_at_tail(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            self.temp_list.append(newNode.data)
        else:
            newNode = Node(data)
            newNode.backward_link = self.tail
            self.tail.forward_link = newNode
            self.tail = newNode
            self.size += 1
            self.temp_list.append(newNode.data)
        return self.temp_list, newNode
    
    def insert_between_nodes(self, data, A, B):
        if A != None and B != None:
            newNode = Node(data)
            A.forward_link = newNode
            newNode.backward_link = A
            newNode.forward_link = B
            B.backward_link = newNode
            return self.traverse_list()
        else:
            return "Either A or B is Null, cannot insert between A and B !, current list is  :" + self.temp_list
    
    def traverse_list(self):
        if self.head == None:
            print("Cannot traverse empty list !")
        current_ptr = self.head
        temp = []
        while current_ptr != None:
            temp.append(current_ptr.data)
            current_ptr = current_ptr.forward_link
        return temp
        

lst = DoublyLinkedList()
ll1, node1 = lst.insert_at_head(34)
ll2, node2 = lst.insert_at_tail(56)
ll3, node3 = lst.insert_at_tail(25)
ll4, node4 = lst.insert_at_tail(16)
ll5, node5 = lst.insert_at_tail(89)
ll6, node6 = lst.insert_at_tail(100)

lst.insert_at_head(34)
print(lst.insert_between_nodes(20,node3,node4))
print("finished")

