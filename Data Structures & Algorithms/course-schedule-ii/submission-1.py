from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for curr, pre in prerequisites:
            adj[pre].add(curr)

        visited = set()
        cycle = set()
        result = []

        def dfs(src):
            nonlocal cycle
            nonlocal visited
            nonlocal result
            if src in cycle:
                return False
            if src in visited:
                return True
            
            cycle.add(src)
            for pre in adj[src]:
                if not dfs(pre):
                    return False
            result = [src] + result
            cycle.remove(src)
            visited.add(src)
            return True
        
        for src in range(numCourses):
            if not dfs(src):
                return []
        return result
        
                

        