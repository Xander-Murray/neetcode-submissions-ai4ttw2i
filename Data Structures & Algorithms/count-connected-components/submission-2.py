class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
          
        # Else recursively find the representative 
        # of the parent
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)

        if irep == jrep:
            return False
            # in same component
        
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        dsu = DSU(n)
        res = n

        for u, v in edges:
            if dsu.unite(u, v):
                res -=1
        return res
            

    