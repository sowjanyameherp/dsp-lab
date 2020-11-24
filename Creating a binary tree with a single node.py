#meher sowjanya, 23
#Creating a binary tree with a single node
#class
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    #print
    def PrintTree(self):
        print(self.data)
tree=Node(23)
#calling print function
tree.PrintTree()
