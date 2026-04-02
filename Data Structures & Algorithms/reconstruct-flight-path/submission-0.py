class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = defaultdict(list)
        for u, v in tickets:
            path[u].append(v)

        for key in path:
            path[key].sort(reverse=True)
        

        currPath = ["JFK"]

        circuit = []
        # list to store the final itinerary

        while len(currPath) > 0:
            currNode = currPath[-1]

            if len(path[currNode]) > 0:

                nextNode = path[currNode].pop()

                currPath.append(nextNode)
            
            else:
                circuit.append(currPath.pop())
    
        

        return circuit[::-1]