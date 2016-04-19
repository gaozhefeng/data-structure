#coding=utf-8
##author: gaozhefeng
##date: 2014-11-04
from Bag import Bag
class Graph:
    '''
       Graph数据结构的实现
       邻接表实现
    '''
    def __init__(self, data):
        ##@param data:graph顶点数目
        ##            或者从文件中获取图的信息
        if isinstance(data, int):
            ##顶点数目和边数
            self.V = data
            self.E = 0
            ##初始化邻接表(空表)
            self.adj = [Bag() for i in range(self.V)]
        else:
            ##从文件中读取图数据
            self.V = int(data.readline())
            self.E = int(data.readline())
            ##初始化邻接表
            self.adj = [Bag() for i in range(self.V)]
            for line in data:
                v, w = line.split(' ')
                self.addEdge(int(v), int(w))

    ##获取graph的顶点数目
    def getVertices(self):
        return self.V
    ##获取graph的边数
    def getEdges(self):
        return self.E

    ##添加一条边集
    def addEdge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)

    ##获得graph中顶点v的邻接表
    def getAdj(self, v):
        return self.adj[v]


    ##定义graph的str属性
    def __str__(self):
        s = str(self.V) + ' vertices, ' + str(self.E) + ' edges\n'
        for v in range(self.V):
            s = s + str(v) + ': '
            for w in self.adj[v]:
                s = s + str(w) + ' '
            s += '\n'

        return s
        

if __name__=='__main__':
    '''test graph structure'''
    with open('tinyG.txt') as f:
        graph = Graph(f)
    tmp = graph.getAdj(0)
    print(list(tmp))
    print(graph)
