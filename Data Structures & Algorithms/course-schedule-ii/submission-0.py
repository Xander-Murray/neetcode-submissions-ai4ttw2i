class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        for a, b in prerequisites:
            dic[a].append(b)

        visit = set()
        visited = set()
        output = []
        def dfs(crs):
            if crs in visit:
                return False

                # found a cycle
            if crs in visited:
                return True

            visit.add(crs)
            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output

