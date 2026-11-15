class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])
        result, heap = [], []
        count, time = 0, tasks[0][0]

        while heap or count < len(tasks):
            if len(heap)==0:
                time = max(tasks[count][0], time)
            while count < len(tasks) and time >= tasks[count][0]:
                task = tasks[count]
                heapq.heappush(heap, (task[1], task[2]))
                count += 1

            offset, tid = heapq.heappop(heap)
            time += offset
            result.append(tid)
        return result
