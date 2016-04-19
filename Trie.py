#!/usr/bin/env python
#coding=utf-8

# This is the implementation of the Trie data structure
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY

class Trie:
	"""docstring for Trie"""
	def __init__(self, strs):
		self.root = {('root'):{}}
		for string in strs:
			self.insert(string, 'root')


	##向trie中添加一个单词
	def insert(self, string, node):
		root = self.root[node]
		l = len(string)
		#tag == 0 means end of string
		tag = [0 if i != l-1 else 1 for i in range(l)]
		for node in zip(string, tag):
			if (node[0], 0) in root:
				node = (node[0], 0)
				root = root[node]
			elif (node[0], 1) in root:
				node = (node[0], 1)
				root = root[node]
			else:
				root[node] = dict()
				root = root[node]
		
	#遍历
	def traverse(self):
		##第一个记录当前最大前缀数目，第二个当前字符数,第三个当前路上的最大prefix
		path = []
		self._traverse(self.root[('root')], path)
		

	def _traverse(self, dic, path):
		for item in dic:
			path.append(item[0])
			
			self._traverse(dic[item], path)
			#遍历到树的叶子
			if item[1] == 1:
				print(path)
			
			path.pop()



if __name__ == '__main__':
	strs = ["gaozhefeng", "gaozheyuan", "luowencui", 'abc', 'abd', 'bcd', 'abcd', 'bcde']
	trie = Trie(strs)
	trie.traverse()
	print(trie.root)
