from Node import Node

class StackUsingLL:

    ''' Stack implementation using Linked List '''
    # All operations are O(1)

    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, data):
        newNode = Node(data)
        
        if self.__head is None:

            self.__head = newNode
            self.__head.next = None
        else:
            
            head = self.__head
            self.__head = newNode
            self.__head.next = head

        self.__count+=1
        return self.__head.data

    def pop(self):
        if self.isEmpty() is True:
            print("Stack is empty!")
            return -1

        ele = self.__head.data
        self.__head= self.__head.next
        self.__count-=1
        return ele

    def top(self):
        if self.isEmpty() is True:
            print("Stack is empty!")
            return -1            
        ele = self.__head.data
        return ele

    def isEmpty(self):
        return self.__count == 0

    def size(self):
        return self.__count

# Initialize the LL based Stack and perform push/pop/top ops

s = StackUsingLL()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

while s.isEmpty() is False:
    print(s.pop())

s.top()

class StackUsingList:

    ''' Stack implementation using Python List '''
    # All operations are O(1)

    def __init__(self):
        self.__arr = []
        self.__head = None
        self.__count = 0
    
    def push(self, data):

        self.__count+=1
        self.__arr.append(data)
        self.__head = self.__arr[self.__count-1]
        return self.__head       

    
    def pop(self):
        if self.isEmpty() is True:
            print("Stack is Empty!")
            return -1

        ele = self.__head
        self.__arr.pop()
        self.__count-=1
        self.__head = self.__arr[self.__count-1] if self.__count > 0 else None
        return ele

    def top(self):
        if self.isEmpty() is True:
            print("Stack is Empty!")
            return -1

        ele = self.__head
        return ele

    def isEmpty(self):
        return self.__count == 0

    def size(self):
        return self.__count

# Initialize the List based Stack and perform push/pop/top ops

sa = StackUsingList()
sa.push(1)
sa.push(2)
sa.push(3)
sa.push(10)

while sa.isEmpty() is False:
    print(sa.pop())

sa.top()