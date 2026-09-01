from collections import defaultdict
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i, j, w in edges:
            adj[i].append((j,w))
            adj[j].append((i,w))
        
        minheap = []
        start = edges[0][0]
        visited = {start}
        heap = []
        output_weights = []

        def push_adj(i):
            for j, w in adj[i]:
                heapq.heappush(heap, (w, i, j))
        push_adj(start)

        while heap:
            w, i, j = heapq.heappop(heap)
            if j not in visited:
                output_weights.append(w)
                visited.add(j)
                push_adj(j)
        if len(visited)<n:
            return -1
        return sum(output_weights) 
