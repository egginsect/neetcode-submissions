import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        idle = [(weight, i) for i, weight in enumerate(servers)]
        busy = []
        heapq.heapify(idle)
        order = []
        time = 0
        for start, task in enumerate(tasks):
            time = max(start, time)
            if not idle:
                time = busy[0][0]
            while busy and time >= busy[0][0]:
                _, sid = heapq.heappop(busy)
                heapq.heappush(idle, (servers[sid], sid))
            _, sid = heapq.heappop(idle)
            heapq.heappush(busy, (time+task, sid))
            order.append(sid)
        return order