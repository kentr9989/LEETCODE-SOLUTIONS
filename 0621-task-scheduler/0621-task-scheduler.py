class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_map = Counter(tasks)
        tasks_heap = [-cnt for cnt in tasks_map.values()]
        heapify(tasks_heap)
        q = deque() # [-cnt, time]
        
        time = 0
        
        while tasks_heap or q:
            time += 1
            if tasks_heap:
                cnt_amt = 1 + heapq.heappop(tasks_heap)
                if cnt_amt:
                    q.append([cnt_amt, time + n])
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(tasks_heap,cnt)
            
        print(f"time: {time}")
        
        return time