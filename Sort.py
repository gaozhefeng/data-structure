#!/usr/bin/env python
#coding=utf-8

# This is the implementation of some common sort algorithms
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY


'''sort module->实现常用的排序算法'''

class Selection:
    '''implementation of selection sort'''
    @classmethod
    def sort(self, lst):
        length = len(lst)
        for i in range(length):
            minVal = i
            for j in range(i+1,length):
                if lst[j] < lst[minVal]:
                    minVal = j
            lst[i], lst[minVal] = lst[minVal], lst[i]
         
class Insertion:
    '''implementation of insertion sort'''
    @classmethod
    def sort(self, lst):
        length = len(lst)
        for i in range(length):
            for j in range(i, 0, -1):
                if lst[j] < lst[j-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                else:
                    break



class Shell:
    '''implementation if shell sort'''
    @classmethod
    def sort(self, lst):
        N = len(lst)
        h = 1
        while h < N//3:
            h = 3*h + 1
        while h >= 1:
            for i in range(h, N):
                for j in range(i, h-1, -h):
                    if lst[j] < lst[j-h]:
                        lst[j],lst[j-h] = lst[j-h],lst[j]
                    else:
                        break
            h //= 3


if __name__ == '__main__':
    l = [6,5,7,8,2,3,1]

    Shell.sort(l)

    print(l)



    
        







    
