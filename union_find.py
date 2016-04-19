#!/usr/bin/env python
#coding=utf-8

# This is the implementation of the union find data structure
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY


##并查集数据结构的三种实现方式
##性能比较:                 union()        find()      
##  quick-find              O(N)           O(1)
##  quick-union             O(树高)       O(树高)
##  weighted-quick-union    O(lgN)         O(lgN)
##

class QuickFindUF(object):
    '''并查集quick-find实现'''
    #初始化操作
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.cnt = n #连通分量数

    #查找节点p所在的连通分量标识
    def find(self, p):
        return self.id[p]

    #判断p，q节点是否连通
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    #p,q不连通，将p,q合并到一个联通分量中去
    def union(self, p, q):
        #分别取得p，q的连通标识符
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        #将所有连通标识符为pid的节点修改为qid
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
        self.cnt -= 1 #少一个连通分量

    #获得连通数目
    def count(self):
        return self.cnt



class QuickUnionUF(object):
    '''并查集quick-union实现'''
    ##初始化    
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.cnt = n


    ##求节点p的祖先根
    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    ##判断节点p,q是否连通
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    ##连通p,q节点
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:#在同一颗树当中
            return
        #将两个节点连接到同一个集合中
        self.id[proot] = qroot
        self.cnt -= 1

    #获得连通数目
    def count(self):
        return self.cnt


class WeightedQuickUnionUF(object):
    '''并查集的weighted-quick-union实现'''
    ##初始化    
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]#记录每棵树的分量大小
        self.cnt = n

    ##求节点p的祖先根
    def find(self, p):
        while p != self.id[p]:
            ##路径压缩算法，将节点的父节点编程爷爷节点
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p


    ##判断节点p,q是否连通
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    ##连通p,q节点
    def union(self, p, q):
        #找到p,q点的根节点
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        ##将较小的树连到大树上
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.cnt -= 1

    #获得连通数目
    def count(self):
        return self.cnt




##test for the union-find module
if __name__ == '__main__':

    l = [(4,3), (3,8), (6,5), (9,4), (2,1), (8,9), (5,0), (7,2), (6,1), (1,0), (6,7)]
    uf = WeightedQuickUnionUF(10)
    for i in l:
        uf.union(i[0],i[1])
        print(uf.id)
        print(uf.count())
    
                
        
