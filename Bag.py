#!/usr/bin/env python

# This is the implementation of the Bag data structure
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY

class Node(object):
	'''
	This is the node class to hold the item
	'''
	def __init__(self, item=None):
		self.item = item
		# the next node 
		self.next = None
	## The presentation of the node
	def __str__(self):
		return str(self.item)



class Bag:
	'''
	The implementation of the Bag.
	The Bag structure is used to collect items.
	It doesn't have the remove method.
	'''
	
	def __init__(self):
		# the first node of the queue
		self.first = None
		# the iterator 
		self.iter = None

		# the numbers of the items in the bag
		self.n = 0
	

	## whether the bag has items
	def is_empty(self):
		return self.first == None
	
	## get the number of the items in the bag.
	def get_size(self):
		return self.n
	
	## add an item into the bag 
	def add(self, item):
		# insert the new node into the front of the queue.
		old_first = self.first
		self.first = Node(item)
		self.first.next = old_first
		# update the iter variable
		self.iter = self.first

	# implement the iterator of the bag structure
	def __iter__(self):
		return self
	
	def next(self):
		if self.iter == None:
			self.iter = self.first
			raise StopIteration
		else:
			item = self.iter.item
			self.iter = self.iter.next
			return item

# test the Bag data structure
if __name__ == '__main__':
	bag = Bag()

	for i in xrange(10):
		bag.add(i)
	
	for item in bag:
		print item

