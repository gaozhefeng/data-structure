#!/usr/bin/env python
#coding=utf-8

# This is the implementation of the knuth shuffle data algorithm
# You can find more information from the book:"Algorithms"
# author: gaozhefeng at XIDIAN UNIVERSITY

import random
class KnuthShuffle:
    '''使用knuth_shuffle方法进行数组的随机排列'''
    @classmethod
    def shuffle(self, l):
        for i in range(len(l)):
            r = random.randint(0,i)
            l[i], l[r] = l[r], l[i]

if __name__ == '__main__':
    l = [0,1,2,3,4,5,6,7,8,9]
    KnuthShuffle.shuffle(l)
    print(l)
