#meher sowjanya , 23
#inserting a node at the end of this doubly linked list   
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class InsertEnd:    
    #Represent the head and tail of the doubly linked list    
    def __init__(self):    
        self.head = None;    
        self.tail = None;    
            
    #addAtEnd() will add a node to the end of the list    
    def addAtEnd(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):    
            self.head = self.tail = newNode;    
            self.head.previous = None;    
            self.tail.next = None;    
        #Add newNode as new tail of the list    
        else:    
            self.tail.next = newNode;    
            newNode.previous = self.tail;    
            self.tail = newNode;    
            self.tail.next = None;    
                
    #display() will print out the nodes of the list    
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Adding a node to the end of the list: ");    
        while(current != None):    
            #Prints each node by incrementing pointer.    
            print(current.data),    
            current = current.next;    
                
        print();    
            
dList = InsertEnd();    
     
#Adding 1 to the list    
dList.addAtEnd(10);    
dList.display();    
#Adding 2 to the list    
dList.addAtEnd(20);    
dList.display();    
#Adding 3 to the list    
dList.addAtEnd(30);    
dList.display();    
#Adding 4 to the list    
dList.addAtEnd(40);    
dList.display();    
#Adding 5 to the list    
dList.addAtEnd(50);    
dList.display();    
