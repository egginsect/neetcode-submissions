from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        visited = set()
        count = 0
        for node in range(n):
            if node in visited:
                continue
            count  += 1
            queue = [node]
            while queue:
                current = queue.pop(0)
                visited.add(current)
                for neighbor in adj[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return count