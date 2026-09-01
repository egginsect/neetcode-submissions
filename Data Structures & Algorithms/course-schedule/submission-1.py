from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        
        for a, b in prerequisites:
            adj[b].add(a)  # Correct direction

        visited = set()
        visiting = set()

        def dfs(src):
            if src in visited:
                return True

            if src in visiting:
                return False

            visiting.add(src)
            for d in adj[src]:
                if not dfs(d):
                    return False
            visiting.remove(src)
            visited.add(src)
            return True

        for s in range(numCourses): 
            if not dfs(s):
                return False

        return True