class DSU:
    def __init__(self,n):
        self.parent = list(range(n + 1))

    def find(self,i):
        if self.parent[i] == i:
            return self.parent[i]
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):

        iRep = self.find(i)

        jRep = self.find(j)

        if iRep == jRep:
            return False
            # already apart of the same componnet

        self.parent[iRep] = jRep
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)

        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                # rest of the points
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))

        # sort by distance
        edges.sort()
        res = 0
        for d, u , v in edges:
            if dsu.union(u, v):
                res += d
            # if we can add to the component add the dist
        return res
