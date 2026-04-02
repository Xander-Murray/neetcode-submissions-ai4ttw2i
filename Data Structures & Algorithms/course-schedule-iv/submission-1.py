class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_map = {i: set() for i in range(numCourses)}
        for c1, c2 in prerequisites:
            course_map[c2].add(c1) # get all the prereqs for a course in a list

        memo = {}

        def is_prereq(pre, course):
            if (pre, course) in memo:
                return memo[(pre, course)]
            
            if pre in course_map[course]:
                memo[(pre, course)] = True
                return True

            for direct_pre in course_map[course]:
                if is_prereq(pre, direct_pre):
                    memo[(pre, course)] = True
                    return True
            memo[(pre, course)] = False
            return False
        
        res = []

        for uj, vj in queries:
            res.append(is_prereq(uj, vj))
        return res
        
