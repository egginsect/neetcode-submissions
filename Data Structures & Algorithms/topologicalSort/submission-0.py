from collections import defaultdict
class Solution:


    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for s,d in edges:
            adj[s].add(d)
        
        result = []
        visited = set()
        visiting = set()
        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False

            visiting.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            visiting.remove(src)
            visited.add(src)
            result.append(src)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        result.reverse()
        return result
        