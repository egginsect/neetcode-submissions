from collections import defaultdict
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]: 
        adj = defaultdict(list)
        visited = set()
        has_cycle = set()
        result = []
        for u, v in edges:
            adj[u].append(v)
        
        def dfs(node):
            if node in has_cycle:
                return True
            if node in visited:
                return False
            visited.add(node)
            has_cycle.add(node)
            for neighbor in adj[node]:
                cycle_detected = dfs(neighbor)
                if cycle_detected:
                    return True
            has_cycle.remove(node)
            result.append(node)
            return False

        for i in range(n):
            cycle_detected = dfs(i)
            if cycle_detected:
                return []
        return result[::-1]