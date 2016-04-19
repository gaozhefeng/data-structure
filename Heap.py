#!/usr/bin/env python
#coding=utf-8

# This is the implementation of the Heap data structure
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY

class Heap:
    '''
       堆的实现(最大堆|最小堆)，默认最大堆
    '''
    def __init__(self, flag='MAX'):
        ##@param flag:标记最大堆或最小堆
        self.pq = [0] #存放元素的数组,第零号元素用来表示队列的大小
        self.flag = flag
        ##堆中用于cmp操作
        self.cmp = {'MAX':self.less, 'MIN':self.large}

    ##判断Heap是否为空
    def isEmpty(self):
        return self.pq[0] == 0

    ##获得Heap的个数
    def getSize(self):
        return self.pq[0]

    ##向Heap中加入新的元素v
    def insert(self, v):
        #在队列尾部加入元素，并且使用swim方法调整优先队列
        self.pq.append(v)
        self.pq[0] += 1
        self.swim(self.pq[0])

    ##删除队列中优先级极值的节点
    def delHeap(self):
        val = self.pq[1]
        self.exch(1,self.pq[0])
        self.pq[0] -= 1
        self.pq.pop()
        self.sink(1)   ##保持优先队列的性质
        return val
    
    
    ##判断i,j元素是否满足less关系
    def less(self, i, j):
        return self.pq[i] <= self.pq[j]

    ##判断i,j元素是否满足large关系
    def large(self, i, j):
        return self.pq[i] >= self.pq[j]
    

    ##交换队列中的i,j元素
    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

     ##swim方法,k为孩子，往上浮动
    def swim(self, k):
        while k>1 and self.cmp[self.flag](k//2,k):
            self.exch(k//2, k)
            k = k//2

    ##sink方法，k为父亲向下沉
    def sink(self, k):
        while 2*k <= self.pq[0]:
            j = 2*k
            ##找到两个孩子中的较大那个
            if j<self.pq[0] and self.cmp[self.flag](j, j+1):
                j += 1
            if not self.cmp[self.flag](k, j):
                break
            self.exch(k, j)
            k = j



if __name__ == '__main__':

    l = [5, 4, 3, 1, 12, 13, 14]
    pq = Heap('MIN')
    for i in l:
        pq.insert(i)

    while not pq.isEmpty():
        print(pq.delHeap())
