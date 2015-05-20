#!/usr/bin/env python

#You can find some informations of the data structure from the book:
#Algorithms by Robert Sedgewick.
# author:gaozhefeng at XIDIAN UNIVERSITY
class Stack(object):
	'''
	Implementation of the basic stack.
	Supports the basic operations:push pop is_empty
	'''

	def __init__(self):
		#the items list is to hold everything in the stack.
		self.items = []

	def push(self, item):
		# push item into the stack
		self.items.append(item)

	def pop(self):
		# pop the item from the stack
		return self.items.pop()
	
	def is_empty(self):
		# judge whether the stack is empty
		return self.items == []
	
	def __str__(self):
		# the method to print the stack. from the bottom to the top.
		return ','.join(map(str, self.items))


if __name__ == '__main__':
	# the test of the stack data structure
	s = Stack()
	s.push(54)
	s.push(12)
	s.push("hello")
	s.push('world')
	print s
