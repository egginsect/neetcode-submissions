from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for i, j, w in edges:
            adj[i].append((j,w))
        shortest_path = {}
        h = [(0, src)]
        while h:
            w1, n1 = heapq.heappop(h)
            if n1 in shortest_path:
                continue
            shortest_path[n1] = w1
            for neighbor, weight in adj[n1]:
                if neighbor not in shortest_path:
                    heapq.heappush(h, (w1+weight, neighbor))
        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1
        return shortest_path