#coding=utf-8
##author: gaozhefeng
##date: 2014-11-07
##update:2014-11-08

from Stack import Stack
from Queue import Queue

class DepthFirstPaths:
    '''
       使用DSF算法寻找所有与源端s连接的顶点及其一条存在的路径
       都是基于单点(s)搜索的
    '''
    def __init__(self, graph, s):
        ##@param graph:图数据结构
        ##@param s:DSF搜索的起点

        ##marked list用于标记vertex是否被访问过
        self.marked = [False for i in range(graph.getVertices())]
        ##用于记录路径
        self.edgeTo = [i for i in range(graph.getVertices())]
        self.s = s##记录源端点

        self.dfs(graph, s)


    ##基于dfs的path搜索
    def dfs(self, graph, v):
        self.marked[v] = True
        ##依次遍历v的邻接表
        for w in graph.getAdj(v):
            if not self.marked[w]:
                ##记录路径
                self.edgeTo[w] = v
                self.dfs(graph, w)

    ##判断s和v之间是否有一条路径相连
    def hasPathTo(self, v):
        return self.marked[v]

    ##返回一条s到v的路径
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None

        ##path为保存路径的栈
        path = Stack()
        while v!=self.s:
            path.push(v)
            v = self.edgeTo[v]
        path.push(self.s)

        return path



class BreadthFirstPaths:
    '''
       基于广度优先搜索算法的路径查找
    '''
    def __init__(self, graph, s):
        ##@param graph:图数据结构
        ##@param s:BSF搜索的起点

        ##marked list用于标记vertex是否被访问过
        self.marked = [False for i in range(graph.getVertices())]
        ##用于记录路径
        self.edgeTo = [i for i in range(graph.getVertices())]
        self.s = s##记录源端点

        self.bfs(graph, s)

    def bfs(self, graph, s):
        ##bfs中使用的队列
        queue = Queue()
        self.marked[s] = True
        queue.enqueue(s)
        while not queue.is_empty():
            ##从queue中删除一个节点
            v = queue.dequeue()
            for w in graph.getAdj(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    queue.enqueue(w)
                    
    ##判断s和v之间是否有一条路径相连
    def hasPathTo(self, v):
        return self.marked[v]

    ##返回一条s到v的路径
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None

        ##path为保存路径的栈
        path = Stack()
        while v!=self.s:
            path.push(v)
            v = self.edgeTo[v]
        path.push(self.s)

        return path
    


if __name__ == '__main__':
    '''test for paths'''
    from Graph import Graph
    with open('tinyGG.txt') as f:
        graph = Graph(f)
    print(graph)
    search = BreadthFirstPaths(graph, 0)
    for v in range(graph.getVertices()):
        print(str(0)+' to '+str(v)+': ',end='')
        if search.hasPathTo(v):
            for x in search.pathTo(v):
                print(str(x),end='') if x==0 else print('-'+str(x),end='')

        print()           
                    
            


    
        
        
        
        
