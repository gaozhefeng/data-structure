#coding=utf-8
##author: gaozhefeng
##date: 2014-11-07
class Node:
    '''linked list nodes'''
    def __init__(self, item=None, next=None):
        self.cargo = item
        self.next = next
    def __str__(self):
        return str(self.cargo)

class Queue:
    '''增加了一个尾节点'''
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
    ##判断queue空
    def is_empty(self):
        return (self.length == 0)

    ##队尾插入节点
    def enqueue(self, item):
        node = Node(item)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1
    ##删除队首节点，并返回节点值
    def dequeue(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo



if __name__ == '__main__':
    '''test for queue'''
    iq = Queue()
    iq.enqueue(1)
    iq.enqueue(2)
    iq.enqueue(3)
    iq.enqueue(4)

    while not iq.is_empty():
        print(iq.dequeue())
