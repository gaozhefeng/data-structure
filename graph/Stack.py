#coding=utf-8
##author: gapzhefeng
##date: 2014-07-15
class Stack:
    '''implementation of stack'''
    def __init__(self):
        self.items = []
        ##用于迭代的变量
        self.iter = -1
        ##stack大小
        self.size = 0
    def push(self, item):
        self.items.append(item)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.items.pop()
    def is_empty(self):
        return (self.items == [])

    ##添加迭代器
    def __iter__(self):
        return self
    def __next__(self):
        if self.iter < -self.size:
            self.iter = -1
            raise StopIteration
        else:
            item = self.items[self.iter]
            self.iter -= 1
            return item
            
        

if __name__=='__main__':
    s = Stack()
    s.push(5)
    s.push(4)
    s.push("+")
    s.push(5)
    s.push(4)
    s.pop()
    s.pop()
    s.push(100)
    for i in s:
        print(i)
    for i in s:
        print(i)
