#coding=utf-8
##author: gaozhefeng
##date: 2014-07-16
class Node:
    '''linked list nodes'''
    def __init__(self, item=None, next=None):
        self.cargo = item
        self.next = next
    def __str__(self):
        return str(self.cargo)

class Queue:
    '''implementation of queue'''
    def __init__(self):
        self.length = 0
        self.head = None
    
    ##判断queue非空
    def is_empty(self):
        return (self.length == 0)

    ##单链表队尾插入节点
    def insert(self, item):
        node = Node(item)
        if self.head == None:
            #if list is empty the new node goes first
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.lenght += 1
    ##删除队首节点，并返回节点值
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo


class ImprovedQueue:
    '''增加了一个尾节点'''
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
    ##判断queue空
    def is_empty(self):
        return (self.length == 0)

    ##队尾插入节点
    def insert(self, item):
        node = Node(item)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1
    ##删除队首节点，并返回节点值
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo



if __name__ == '__main__':
    iq = ImprovedQueue()
    iq.insert(1)
    iq.insert(2)
    iq.insert(3)
    iq.insert(4)

    while not iq.is_empty():
        print(iq.remove())

