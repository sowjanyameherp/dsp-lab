#meher sowjanya, 23
#Tree Cutsom problem
#with 2 functions and one of these being a recursive function

#Printing Subtrees

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def insertNodes(self,data):
		node = Node(data)
		q = []
		if self.root == None:
			self.root = node
		else:
			q.append(self.root)

		while len(q) != 0:
			n = q.pop(0)
			if n.left == None:
				n.left = node
				break
			else:
				q.append(n.left)
			if n.right == None:
				n.right = node
				break
			else:
				q.append(n.right)

	def printNodes(self,root):
		q = []
		a = []
		if root == None:
			return
		if root != None:
			q.append(root)
		while len(q) > 0:
			a.append(q[0].data)
			node = q.pop(0)

			if node.left != None:
				q.append(node.left)
			if node.right != None:
				q.append(node.right)
		print ("Tree:",a)

	def subTrees(self,root):
		if root == None:
			return
		l = root.left
		r = root.right
		def left(node,le): 
			if node:
				le.append(node.data)
				left(node.left, le)
				left(node.right, le)
			return le
		def right(node,ri): 
			if node:
				ri.append(node.data)
				right(node.left, ri)
				right(node.right, ri)
			return ri
		p = []
		q = []
		p = left(l,p)
		q = right(r,q)

		print("Subtree- left: ",p)
		print("Subtree- right: ",q)


B = BinaryTree()
n = int(input("Enter no.of nodes: "))
print("Enter node values: ")
for i in range(n):
	k = int(input())
	B.insertNodes(k)

B.printNodes(B.root)
B.subTrees(B.root)
