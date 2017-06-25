"""

Binary Search Tree implementation in Python
All the functions are iterative.

"""

class Node(object):

	""" Class of Node """

	def __init__(self, key, left=None, right=None):
		"""Constructor for a Node.

		Params:
			key: data value for the node
			left: left child for the node 
			right:	right child for the node		
		"""

		self.key = key
		self.left = left
		self.right = right

	def __str__(self):
		return "Node(key: {0}, left: {1}, right: {2})" \
				.format(
					self.key, 
					self.left.key if self.left!=None else None,
					self.right.key if self.right!=None else None)

class BST:
	""" Class of BinarySearchTree """

	def __init__(self, key):
		"""Constructor for a BST.

		Params: 
			key: data value for the first node
		
		"""
		self.root = Node(key)

	def addNode(self, key):
		"""Adds another node to the tree.

		Params:
			key: data value of the new node

		"""

		node = self.root
		while (node != None):
			if (key <= node.key):
				if (node.left == None):
					node.left = Node(key)
					break
				else:
					node = node.left
			else:
				if (node.right == None):
					node.right = Node(key)
					break
				else:
					node = node.right

	def search(self, key):
		"""Search the key in the tree.

		Param:
			key: data value for node to be searched

		Returns:
			The search result
		"""

		node = self.root
		while (node != None):
			if (key == node.key):
				return node
			elif (key < node.key):
				node = node.left
			else:
				node = node.right
		return node

	def findMin(self):
		"""Return the minimum key in the BST

		Returns:
			The minimum key
		"""

		node = self.root
		while (node.left != None):
			node = node.left
		return node

	def findMax(self):
		"""Return the maximum key in the BST

		Returns:
			node: The maximum key
		"""

		node = self.root
		while (node.right != None):
			node = node.right
		return node

	def succ(self, keyNode):
		"""The in-order successor to the node
		
		Param:
			keyNode: node value

		Returns:
			node: in-order successor
		"""

		node = keyNode.right
		while (node.left is not None):
			node = node.left
		return node

	def findParent(self, key):
		"""Return the parent of the key node
		
		Params:
			key: node value 

		Returns:
			node: parent node of the key value node
		"""

		parent, node = None, self.root
		while True:
			if node is None:
				return None

			if node.key == key:
				return parent

			if node.key > key:
				parent, node = node, node.left
			else:
				parent, node = node, node.right

	def deleteNode(self, key):
		"""Delete the key from the BST

		Param:
			key: the key to be deleted
		"""

		parent = self.findParent(key)
		delt = parent.left if (parent.left is not None and parent.left.key == key) else parent.right
		while (delt is not None):
			if delt.left is None and delt.right is None:
				if parent.left == delt:
					parent.left = None
				else:
					parent.right = None
				delt = None
			elif delt.left is None or delt.right is None:
				if delt.left is None:
					delt.key = delt.right.key
					parent, delt = delt, delt.right
				else:
					delt.key = delt.left.key
					parent, delt = delt, delt.left
			else:
				succ = self.succ(delt)
				delt.key = succ.key
				parent, delt = delt, succ

if __name__ == "__main__":

	print "*** Insertion ***"
	bst = BST(10)
	bst.addNode(2)
	bst.addNode(4)
	bst.addNode(6)
	bst.addNode(14)
	bst.addNode(16)
	bst.addNode(12)

	print "*** Search ***"
	print bst.search(10)
	print bst.search(14)
	print bst.search(15)

	print "*** Min/Max ***"
	print bst.findMin()
	print bst.findMax()

	print "*** Deletion ***"
	bst.deleteNode(14)

	print "*** Parent ***"
	print bst.findParent(16)