from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        buf = []
        out = []

        for i in range(numCourses):
            if indegree[i] == 0:
                buf.append(i)
        while buf:
            course = buf.pop()
            out.append(course)
            for dependent in adj[course]:
                if indegree[dependent] > 0:
                    indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    buf.append(dependent)
                    del indegree[dependent]
        return len(out) == numCourses
