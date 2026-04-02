class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur_load = 0
        heap = []


        trips.sort(key=lambda x: x[1]) # sort by start point

        for num, start, end in trips:
            while heap and  start >= heap[0][0]:
                drop_end, drop_num = heapq.heappop(heap)
                cur_load -= drop_num
            
            heapq.heappush(heap, (end, num))
            cur_load += num
            
            if cur_load > capacity:
                return False

        return True

        