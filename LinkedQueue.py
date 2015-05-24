#!/usr/bin/env python

# You can find some very useful information from the book:
# Algorithms by Robert Sedgewick
# author: gaozhefeng at XIDIAN UNIVERSITY

class Node(object):
	'''
	This Node class is used as a node in the linked list.	
	'''
	# @param cargo, the value that the node should holds
	# @param next, the next node behind the current node.
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next
	
	# to represent the node.
	def __str__(self):
		return str(self.cargo)


class LinkedQueue(object):
	'''
	Use linked list to implement the basic queue.	
	'''
	
	def __init__(self):
		# record the length of the queue
		self.length = 0
		# the first node in the linked list
		self.head = None
	
	# judge whether the queue is empty
	def is_empty(self):
		return self.length == 0
	
	# insert the node in the rear of the queue
	def insert(self, item):
		node = Node(item)
		if self.head == None:# the queue is empty
			self.head = node
		else:
			last = self.head
			while last.next:# find the last node in the quue
				last = last.next
			last.next = node
		self.length += 1
	
	# remove the node from the head, and return the value of the head node
	def remove(self):
		item = self.head.cargo
		self.head = self.head.next
		self.length -= 1
		return item
	
	# the represent of the queue. print the node from head to rear
	def __str__(self):
		current = self.head
		items = []
		while current:
			items.append(str(current))
			current = current.next
		return '->'.join(items)

if __name__ == '__main__':
	# some simple test for the queue based on the linked list
	queue = LinkedQueue()
	queue.insert(1)
	queue.insert(2)
	queue.insert(3)
	queue.insert(4)
	print "after insert 1,2,3,4 the queue now is:"
	print "length of the queue:", queue.length
	print queue
	queue.remove()
	queue.remove()
	print "after remove two elements, the queue now is:"
	print "length of the queue:", queue.length

	print queue


