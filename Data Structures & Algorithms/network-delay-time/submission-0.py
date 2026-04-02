class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        paths = defaultdict(list)
    
        for u, v, time in times:
            paths[u].append((v,time))
            
        
        dist = [float('inf')] * (n + 1)

        pq = []
        heapq.heappush(pq, (0, k))
        

        dist[k] = 0
        



        # while we still have nodes to reach and calculate the distance
        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in paths[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
        result = max(dist[1:])
        
        # If result is infinite, someone didn't get the message
        return -1 if result == float('inf') else result




        
        


        