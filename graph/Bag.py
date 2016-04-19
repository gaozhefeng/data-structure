#coding=utf-8
##author: gaozhefeng
##date: 2014-11-04

class Node:
    '''
       链表节点的表示
    '''
    def __init__(self, item=None):
        self.item = item
        self.next = None

class Bag:
    '''
       Bag 数据结构的实现
       Bag是一种不支持删除元素的集合数据结构。Bag的主要
       目的是收集元素并迭代所有收集到的元素
    '''
    def __init__(self):
        ##队列首元素
        self.first = None
        ##用于迭代
        self.iter = None
        ##bag中元素的大小
        self.N = 0

    ##判断bag是否为空
    def isEmpty(self):
        return self.first==None

    ##获得bag中元素的大小
    def getSize(self):
        return self.N

    ##想bag中添加元素item
    def add(self, item):
        oldFirst = self.first
        self.first = Node(item)
        self.first.next = oldFirst
        ##更新迭代器
        self.iter = self.first

    ##实现bag的iter接口
    def __iter__(self):
        return self

    def __next__(self):
        if self.iter is None:
            self.iter = self.first
            raise StopIteration
        else:
            item = self.iter.item
            self.iter = self.iter.next
            return item



if __name__=="__main__":
    '''test for Bag data structure'''
    bag = Bag()
    for i in range(10):
        bag.add(i)
    print(bag.first)
    
    for item in bag:
        print(item)

    print(bag.first)
    
        
        
        
        
    
