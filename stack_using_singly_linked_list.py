class Node:
    def __init__(self,info,link =None):
        self.info = info
        self.link = link

class LinkedStack:
    def __init__(self):
        self.head= None
        self.current_ptr= None
        self.size = 0
        self.tempLst =[]        # created just to test if LinkedStack working properly(Not compulsory)
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self,item):
        if self.head == None:
            newNode = Node(item)
            newNode.link = None
            self.head = newNode
            self.size += 1
            self.tempLst.append(item)
        else:
            newNode = Node(item)
            newNode.link = self.head
            self.head = newNode
            self.size += 1
            self.tempLst.append(item)
        return self.tempLst

    def top(self):
        if self.head == None:
            print('Stack empty ! cannot return top element')
        return self.head.info
    
    def pop(self):
        if self.isEmpty():
            print('Stack empty ! cannot pop')
        item = self.head.info
        temp_pointer= self.head
        self.head = self.head.link
        temp_pointer.link =None
        self.size -= 1
        return item

s= LinkedStack()
print(s.push(4))
print(s.push(9))
print(s.push(8))
print(s.push(3))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

        

        
        
