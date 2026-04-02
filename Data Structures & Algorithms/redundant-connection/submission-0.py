class Dsu:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, i):
        if self.parent[i] == i:
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        irep = self.find(i)

        jrep = self.find(j)

        if irep == jrep:
            return False

        self.parent[irep] = jrep
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            graph = Dsu(len(edges))
            
            # build the graph as a disjoint set
            for u, v in edges:
                if not graph.union(u, v):
                    return [u,v]

            