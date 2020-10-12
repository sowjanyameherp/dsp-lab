#counting number of nodes in linked list
# Node class 
class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None   
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    #new node at the beginning of Linked List. 
    def push(self, new_data): 
  
        new_node = Node(new_data) 
  
        new_node.next = self.head
        
        self.head = new_node 
  
    # This function counts number of nodes in Linked List 
    def getCountRec(self, node): 
        if (not node): 
            return 0
        else: 
            return 1 + self.getCountRec(node.next) 
  
    def getCount(self): 
       return self.getCountRec(self.head) 
  
# Code execution starts here 
if __name__=='__main__': 
    llist = LinkedList() 
    llist.push(1) 
    llist.push(3) 
    llist.push(1) 
    llist.push(2) 
    llist.push(1)
    llist.push(3)
    print ('Count of nodes is :',llist.getCount()) 
