import sys

MAX_NUM = sys.maxsize

class Graph:
    def __init__(self):
        """初始化一个空的无向图"""
        self.adj = {}

    def add_node(self, node):
        """添加一个节点"""
        if node not in self.adj:
            self.adj[node] = []
    
    def add_edge(self, node1, node2, weight):
        """添加一条边"""
        self.add_node(node1)
        self.add_node(node2)
        self.adj[node1].append((node2, weight))
        self.adj[node2].append((node1, weight))

    def get_nodes(self):
        """返回所有顶点"""
        return list(self.adj.keys())
    
    def get_edges(self):
        """"返回所有边"""
        result = []
        for node in self.adj:
            for neighbor, weight in self.adj[node]:
                if (neighbor, node, weight) not in result:
                    result.append((node, neighbor, weight))
        return result
    
def get_MinWeight(dict):
    """获取当前字典中值最小的元素

    input: 字典

    return: 最小元素
    """
    min = MAX_NUM
    res = ''
    for key, value in dict.items():
        if value < min:
            res = key
            min = value
    return (res, min)


def dijstrsa(graph: Graph, start):
    """dijstra算法
    
    input: 无向图，起始节点

    return: 起始点到其他点的最短距离(字典)
    """
    selected = {}
    unselected = {}
    edges = graph.get_edges()

    #初始化最短路径数组和未选取数组
    for node in graph.get_nodes():
        if node == start:
            selected[node] = 0
        else:
            unselected[node] = MAX_NUM
    
    #遍历未选取的节点
    for i in range(len(unselected)):
        current = next(reversed(selected))
        #遍历当前点与邻点的距离，是否小于现有距离
        for node1, node2, weight in edges:
            if node1 == current and node2 not in selected:
                if weight+selected[current] < unselected[node2]:
                    unselected[node2] = weight+selected[current]
            elif node2 == current and node1 not in selected:
                if weight+selected[current] < unselected[node1]:
                    unselected[node1] = weight+selected[current]
        (key, weight) = get_MinWeight(unselected)
        selected[key] = weight
        del unselected[key]

    return selected


    
if __name__ == "__main__":
    graph = Graph()
    array = [['A', 'B', 12], ['A', 'F', 16], ['A', 'G', 14],
             ['B', 'F', 7], ['B', 'C', 10], ['G', 'F', 9],
             ['G', 'E', 8], ['F', 'C', 6], ['F', 'E', 2],
             ['C', 'E', 5], ['C', 'D', 3], ['E', 'D', 4],]
    start_node = 'D'
    for node1, node2, weight in array:
        graph.add_edge(node1, node2, weight)

    for node, distance in dijstrsa(graph, start_node).items():
        print(f"从{start_node}到{node}的最短距离: {distance} \n")