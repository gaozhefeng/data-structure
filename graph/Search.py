#coding=utf-8
##author: gaozhefeng
##date: 2014-11-05
class DFS:
    '''
       DFS深度优先搜索算法的实现
    '''
    def __init__(self, graph, s):
        ##@param graph:图数据结构
        ##@param s:DSF搜索的起点
        ##marked list用于标记vertex是否被访问过
        self.marked = [False for i in range(graph.getVertices())]
        ##与s连通顶点个数
        self.count = 0
        self.dfs(graph, s)
    
    def dfs(self, graph, v):
        self.marked[v] = True
        self.count += 1
        for w in graph.getAdj(v):
            ##没有被访问过，递归调用dfs
            if not self.isMarked(w):
                self.dfs(graph, w)
            
    ##顶点w是否被标记过
    def isMarked(self, w):
        return self.marked[w]

    ##获得与s连通顶点的个数
    def getCount(self):
        return self.count


if __name__=='__main__':
    '''test for the DFS'''
    from Graph import Graph
    with open('tinyG.txt') as f:
        graph = Graph(f)

    s = DFS(graph, 9)
    for v in range(graph.getVertices()):
        if s.isMarked(v):
            print(str(v)+' ',end='')

    print(s.getCount())
