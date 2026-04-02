class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)

        for a, b in prerequisites:
            dic[a].append(b)

        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
                # found a cycle
            if dic[crs] == []:
                return True

            visit.add(crs)
            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            dic[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



        