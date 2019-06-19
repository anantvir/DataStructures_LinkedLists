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
        return newNode

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
        return newNode

    def insert_item_between_nodes(self,item,LOCA,LOCB):     # LOCA = predecessor, LOCB = Successor
        newNode = Node(item)
        newNode.FORWARD_LINK = LOCB
        newNode.BACKWARD_LINK = LOCA
        LOCA.FORWARD_LINK = newNode
        LOCB.BACKWARD_LINK = newNode
        return newNode
    
    def traverse_list(self):
        if self.head == None:
            print('Cant traverse. List is Empty !')
        temp_head = self.head
        while self.head != None:
            print(self.head.info)
            self.head = self.head.FORWARD_LINK
        self.head = temp_head

#-Author - Anantvir Singh-----Reference = DS ALgo by Michael T. Goodrich et al
class PositionalList(DoublyLinkedList):

    #---------------Each node is represented by an abstraction called Position, which returns a user friendly position object encapsulating a node ------------------
    class Position:     # Nested class
        def __init__(self,container,node):
            self._container = container
            self._node = node
        
        def info(self):
            return self._node.info
        
        def __eq__(self,other):
            return type(other) is type(self) and other.node is self._node

    #--------------------------Validate if position given by user is correct ---------------------------------
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('p is not of type Position !')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.FORWARD_LINK is None:
            raise ValueError('p is not valid. It is a sentinel !')
        return p._node
    
    #--------------Utility method to create a new Position object(Wrap node in this object) and return it-------------------------------
    def _make_position(self,node):
        if node is self.head or node is self.tail:
            return None
        else:
            return self.Position(self,node)     # returns position of node given to this method

    def first(self):                            # returns position of 1st node i.e node after the header
        return self._make_position(self.head.FORWARD_LINK)
    
    def last(self):
        return self._make_position(self.tail.BACKWARD_LINK)
    
    def before(self,p):
        node = self._validate(p)
        return self._make_position(node)
    
    def after(self,p):
        node = self._validate(p)
        return self._make_position(node)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.info()
            cursor = self.after(cursor)

        #-----------------------List modification methods----------------------------
    
    def insert_item_between_nodes(self,item,LOCA,LOCB):
        node = super().insert_item_between_nodes(item,LOCA,LOCB)
        return self._make_position(node)

    def insert_in_front(self,item):
        return self.insert_item_between_nodes(item,self.head,self.head.FORWARD_LINK)
    
    def insert_at_last(self,item):
        return self.insert_item_between_nodes(item,self.tail,self.tail.BACKWARD_LINK)

    def add_before(self,position,item):     # insert 'item' before 'position'
        node_for_given_position = self._validate(position)
        return self.insert_item_between_nodes(item,node_for_given_position.BACKWARD_LINK,node_for_given_position)
    
    # Similarly more methods can be implemented like 'add_after' or other modification methods also called 'mutators'
    
