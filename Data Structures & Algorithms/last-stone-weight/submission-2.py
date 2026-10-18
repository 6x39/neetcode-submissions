import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap) #largest value now at front, but is negative, so need to multiply by -1 for any future stuff to do with it.
        while len(max_heap) > 1:
            element1 = heapq.heappop(max_heap) * -1
            element2 = heapq.heappop(max_heap) * -1
            if element1 < element2:
                element2 = element2 - element1
                heapq.heappush(max_heap, element1 * -1)
            elif element1 > element2:
                element1 = element1 - element2
                heapq.heappush(max_heap, element1 * -1)
        if len(max_heap) == 1:
            return heapq.heappop(max_heap) * -1
        else:
            return 0


        