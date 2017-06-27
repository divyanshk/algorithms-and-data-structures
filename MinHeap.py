"""

A MinHeap implementation in Python

"""

from sys import maxint
MIN_INT = -maxint-1

class MinHeap(object):

	""" Class of MinHeap """

	def __init__(self):
		self.heap = []

	def parentIndex(self, i):
		return (i-1)/2 if (i-1)/2 >= 0 else None

	def leftChildIndex(self, i):
		return 2*i if 2*i < len(self.heap) else None

	def rightChildIndex(self, i):
		return 2*i+1 if 2*i+1 < len(self.heap) else None

	def getMinimum(self):
		return self.heap[0]

	def extractMinimum(self):
		minimum = self.heap[0]
		lastElem = self.heap.pop()
		if len(self.heap) > 0:
			self.heap[0] = lastElem
			self.heapifyOnIndex(0)
		return minimum

	def decreaseKey(self, index, newValue):
		self.heap[index] = newValue
		self.fixHeap(index)

	def insert(self, value):
		self.heap.append(value)
		index = len(self.heap)-1
		self.fixHeap(index)

	def delete(self, index):
		self.decreaseKey(index, MIN_INT)
		self.extractMinimum()

	def fixHeap(self, index):
		try:
			# print self.heap
			while (index != 0 and self.heap[index] < self.heap[self.parentIndex(index)]):
				self.heap[index] , self.heap[self.parentIndex(index)] = self.heap[self.parentIndex(index)], self.heap[index]
				index = self.parentIndex(index)
		except TypeError as e:
			raise TypeError("Trying to access a memory location which doesn't exist.")

	def heapifyOnIndex(self, index):
		left = self.leftChildIndex(index)
		right = self.rightChildIndex(index)
		smallest = index
		if (left != None and self.heap[left] < self.heap[index]):
			smallest = left
		if (right != None and self.heap[right] < self.heap[smallest]):
			smallest = right
		if smallest != index:
			self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
			self.heapifyOnIndex(smallest)

if __name__ == "__main__":

	heap = MinHeap()
	heap.insert(3)
	heap.insert(2)
	heap.delete(1)
	heap.insert(15)
	heap.insert(5)
	heap.insert(4)
	heap.insert(45)
	print heap.extractMinimum()
	print heap.getMinimum()
	heap.decreaseKey(index=2, newValue=1)
	print heap.getMinimum()
