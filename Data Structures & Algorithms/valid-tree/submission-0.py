class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        paths = defaultdict(list)

        for u, v in edges:
            paths[u].append(v)
            paths[v].append(u)
        
        visit = set()
        def dfs(u, prev):
            if u in visit:
                return False # Real cycle detected
            
            visit.add(u)
            for v in paths[u]:
                # CRITICAL FIX: If neighbor is where we just came from, ignore it
                if v == prev:
                    continue
                
                if not dfs(v, u):
                    return False
            return True

        # 1. Run DFS starting from node 0
        # We pass -1 as prev because 0 has no parent
        if not dfs(0, -1):
            return False
        
        # 2. Check Connectivity
        # A valid tree must be fully connected (no islands)
        # If we visited fewer nodes than 'n', some nodes are unreachable.
        return len(visit) == n