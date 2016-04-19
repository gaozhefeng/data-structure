#!/usr/bin/env python
#coding=utf-8

# This is the implementation of the Bag data structure
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY
class Node:
	'''
	BST中的节点结构
	'''

	def __init__(self, key, val, N):

		self.key = key
		self.val = val		##节点中的键值对
		self.left = None
		self.right = None	##节点的左右子树
		self.N = N          ##以该节点为根节点的树的总结点数目,在rank和select方法中起到作用

class BST:
	'''
	BST的实现
	'''

	def __init__(self):
		#根节点(私有成员)
		self.__root = None  

	##返回BST中的所有节点
	def size(self):
		return self.__size(self.__root)

	##私有成员函数，返回某节点为二叉树的所有节点
	def __size(self, x):
		if x:##树非空
			return x.N
		else:
			return 0


	##BST中存在key则返回相应的val，否则返回None
	def get(self, key):
		return self.__get(self.__root, key)

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


	##把以key-val为键值对插入BST中。key已存在的话，更新val
	def put(self, key, val):
		self.__root = self.__put(self.__root, key, val)

	##在以x为根节点的BST中插入key-val节点
	def __put(self, x, key, val):
		if x==None:##空BST,生成一个节点
			return Node(key, val, 1)

		if key < x.key:
			x.left = self.__put(x.left, key, val)
		elif key > x.key:
			x.right = self.__put(x.right, key, val)
		else:##key已经存在于BST中，更新val值
			x.val = val
		##更新N的值
		x.N = self.__size(x.left) + self.__size(x.right) + 1
		return x

	##取得BST中的最小键值
	def min(self):
		return self.__min(self.__root).key

	##取得以x为根节点的BST中的最小节点
	##返回最小节点的引用
	def __min(self, x):
		if x.left==None:
			return x
		else:
			return self.__min(x.left)

	##取得BST中的最大键值
	def max(self):
		return self.__max(self.__root).key


	##取得以x为根节点的BST中的最大节点
	##返回最大节点的引用
	def __max(self, x):
		if x.right==None:
			return x
		else:
			return self.__max(x.right)

	
	##在BST中查找键值小于等于key的最大key
	def floor(self, key):
		x = self.__floor(self.__root, key)
		if x:
			return x.key
		else:
			return None

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

	##在BST中查找键值大于等于key的最小key
	def ceiling(self, key):
		x = self.__ceiling(self.__root, key)
		if x:
			return x.key
		else:
			return None
		
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

	##在BST中返回排名为k的节点的key
	def select(self, k):
		return self.__select(self.__root, k).key


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

	##返回键值key在BST中的排名(从0开始计数)
	def rank(self, key):
		return self.__rank(self.__root, key)

	def __rank(self, x, key):
		if x==None:##空BST
			return -1
		if key<x.key:
			return self.__rank(x.left, key)
		elif key>x.key:
			return 1 + self.__size(x.left) + self.__rank(x.right, key)
		else:
			return self.__size(x.left)


	##删除最小节点
	def deleteMin(self):
		self.__root = self.__deleteMin(self.__root)

	def __deleteMin(self, x):
		if x.left==None:##节点没有左子树，x节点就是最小节点，删除！
			ans = x.right
			del x   ##释放空间
			return ans
		x.left = self.__deleteMin(x.left)
		x.N = self.__size(x.left) + self.__size(x.right) + 1
		return x


	##删除最大节点
	def deleteMax(self):
		self.__root = self.__deleteMax(self.__root)

	def __deleteMax(self, x):
		if x.right==None:##节点没有右子树，x节点就是最大节点，删除！
			ans = x.left
			del x   ##释放空间
			return ans
		x.right = self.__deleteMax(x.right)
		x.N = self.__size(x.left) + self.__size(x.right) + 1
		return x

	##在BST中删除键值为key的节点
	def delete(self, key):
		self.__root = self.__delete(self.__root, key)


	def __delete(self, x, key):
		if x==None:
			return None
		if key<x.key:##在左子树中进行删除操作
			x.left = self.__delete(x.left, key)
		elif key>x.key:##在右子树中进行删除
			x.right = self.__delete(x.right, key)
		else:
			##删除节点中只有一个分支，和deleteMin(),deleteMax()处理一样
			if x.right==None:
				ans = x.left
				del x
				return ans
			if x.left==None:
				ans = x.right
				del x
				return ans


			##删除节点有两个子树，Hibbard方法
			t = x
			x = self.__min(t.right)
			x = Node(x.key, x.val, x.N)
			x.right = self.__deleteMin(t.right)
			x.left = t.left
			del t
		x.N = self.__size(x.left) + self.__size(x.right) + 1
		return x


	##BST的遍历
	def traversal(self):
		self.__traversal(self.__root)

	##中序遍历x节点
	def __traversal(self, x):
		if x:
			self.__traversal(x.left)
			print('%c:%d'%(x.key,x.val))
			self.__traversal(x.right)




if __name__ == '__main__':
	
	bst = BST()
	bst.put('S',0)
	bst.put('E',1)
	bst.put('A',2)
	bst.put('R',3)
	bst.put('C',4)
	bst.put('H',5)
	bst.put('E',6)
	bst.put('X',7)
	bst.put('A',8)
	bst.put('M',9)
	bst.put('P',10)
	bst.put('L',11)
	bst.put('E',12)
	# print(bst.rank('P'))
	bst.delete('S')

	# bst.delete('M')
	# print(bst.max())
	# print(bst.min())
	# print(bst.floor('Q'))
	# print(bst.ceiling('G'))
	# print(bst.select(7))
	# print(bst.rank('E'))
	# bst.deleteMax()
	# bst.delete('L')
	# bst.deleteMax()
	# bst.deleteMin()
	# bst.delete('E')
	# bst.deleteMax()
	
	

	bst.traversal()
	print(bst.rank('P'))