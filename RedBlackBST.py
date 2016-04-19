#!/usr/bin/env python
#coding=utf-8

# This is the implementation of the RedBlack BST data structure
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY


## RB树中的红黑节点颜色表示
RED = True
BLACK = False

class Node:
	"""RB树中的节点表示"""
	def __init__(self, key, val, N, color):
		##节点的键值对
		self.key = key
		self.val = val
		##节点为子树的大小
		self.N = N
		##左右子树
		self.left = None
		self.right = None
		##节点的颜色
		self.color = color



class RedBlackBST:
	"""红黑树的实现"""
	def __init__(self):
		self.root = None ##BST根节点

	##判断结点x是否为红色
	def __isRed(self, x):
		if x==None:
			return False
		return x.color == RED

	##私有成员函数，返回某节点为二叉树的所有节点
	def __size(self, x):
		if x:##树非空
			return x.N
		else:
			return 0

	##从节点x开始查找是否存在键key
	def __get(self, x, key):
		if x:##非空节点时
			if key < x.key:##递归查询左子树
				return self.__get(x.left, key)
			elif key > x.key:##递归查询右子树
				return self.__get(x.right, key)
			else:##查询成功
				return x.val
		else:
			return None

	##取得以x为根节点的BST中的最小节点
	##返回最小节点的引用
	def __min(self, x):
		if x.left==None:
			return x
		else:
			return self.__min(x.left)

	##取得以x为根节点的BST中的最大节点
	##返回最大节点的引用
	def __max(self, x):
		if x.right==None:
			return x
		else:
			return self.__max(x.right)


	def __floor(self, x, key):
		if x==None:
			return None
		if key==x.key:
			return x
		elif key<x.key:
			return self.__floor(x.left, key)
		##一直沿着左子树走下去

		##查看又子树是否存在相应的key
		t = self.__floor(x.right, key)
		if t:
			return t
		else:
			return x

	def __ceiling(self, x, key):
		if x==None:
			return None
		if key==x.key:
			return x
		elif key>x.key:
			return self.__ceiling(x.right, key)
		##一直沿着右子树走下去

		##查看左子树是否存在相应的key
		t = self.__ceiling(x.left, key)
		if t:
			return t
		else:
			return x

	##私有成员函数，返回以x为根节点中排名为k的节点
	def __select(self, x, k):
		if x==None:##空BST
			return None
		t = self.__size(x.left)##左子树的节点数目
		if t>k:##目标在左子树中
			return self.__select(x.left, k)
		elif t<k:##目标在右子树中
			return self.__select(x.right, k-t-1)
		else:
			return x


	def __rank(self, x, key):
		if x==None:##空BST
			return -1
		if key<x.key:
			return self.__rank(x.left, key)
		elif key>x.key:
			return 1 + self.__size(x.left) + self.__rank(x.right, key)
		else:
			return self.__size(x.left)

	##将结点为h处进行左旋转
	def __rotateLeft(self, h):

		x = h.right
		h.right = x.left
		x.left = h
		x.color = h.color
		h.color = RED
		x.N = h.N
		h.N = 1 + self.__size(h.left) + self.__size(h.right)
		return x
		

	##将结点h处进行右旋转
	def __rotateRight(self, h):
		x = h.left
		h.left = x.right
		x.right = h
		x.color = h.color
		h.color = RED
		x.N = h.N
		h.N = 1 + self.__size(h.left) + self.__size(h.right)
		return x

	##结点h处进行颜色变换
	def __flipColors(self, h):
		h.color = RED
		h.left.color = BLACK
		h.right.color = BLACK

	##在以h为根节点的树中插入key-val结点
	def __put(self, h, key, val):
		if h==None:##插入一个红节点
			return Node(key, val, 1, RED)

		if key < h.key:
			h.left = self.__put(h.left, key, val)
		elif key > h.key:
			h.right = self.__put(h.right, key, val)
		else:
			h.val = val

		if self.__isRed(h.right) and not self.__isRed(h.left):
			h = self.__rotateLeft(h)
		if self.__isRed(h.left) and self.__isRed(h.left.left):
			h = self.__rotateRight(h)
		if self.__isRed(h.left) and self.__isRed(h.right):
			self.__flipColors(h)
		h.N = 1 + self.__size(h.left) + self.__size(h.right)
		return h


	##返回BST中的所有节点
	def size(self):
		return self.__size(self.root)

	##BST中存在key则返回相应的val，否则返回None
	def get(self, key):
		return self.__get(self.root, key)

	##取得BST中的最小键值
	def min(self):
		return self.__min(self.root).key

	##取得BST中的最大键值
	def max(self):
		return self.__max(self.root).key

	##在BST中查找键值小于等于key的最大key
	def floor(self, key):
		x = self.__floor(self.root, key)
		if x:
			return x.key
		else:
			return None
	##在BST中查找键值大于等于key的最小key
	def ceiling(self, key):
		x = self.__ceiling(self.root, key)
		if x:
			return x.key
		else:
			return None
	##在BST中返回排名为k的节点的key
	def select(self, k):
		return self.__select(self.root, k).key

	##返回键值key在BST中的排名(从0开始计数)
	def rank(self, key):
		return self.__rank(self.root, key)

	##添加key-val结点到RB树中
	def put(self, key, val):
		self.root = self.__put(self.root, key, val)
		self.root.color = BLACK  ##根节点颜色始终为黑色


	##BST的遍历
	def traversal(self):
		self.__traversal(self.root)

	##中序遍历x节点
	def __traversal(self, x):
		if x:
			self.__traversal(x.left)
			print('%c:%d'%(x.key,x.val))
			self.__traversal(x.right)




if __name__ == '__main__':
	'''delete操作还没实现'''
	rbt = RedBlackBST()
	rbt.put('S',1)
	rbt.put('E',1)
	rbt.put('A',1)
	rbt.put('R',1)
	rbt.put('C',1)
	rbt.put('H',1)
	rbt.put('X',1)
	rbt.put('M',1)
	rbt.put('P',1)
	rbt.put('L',1)
	rbt.traversal()
	print(rbt.select(5))
	print(rbt.rank('L'))
	print(rbt.size())
	print(rbt.max())
	print(rbt.min())
	print(rbt.floor('F'))
	print(rbt.ceiling('F'))
	print(rbt.get('P'))


