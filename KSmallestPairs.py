# Problem: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for i in nums1:
            for j in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-i-j, (i,j)))
                else:
                    if -heap[0][0] > (i+j):
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-i-j, (i,j)))
        return map(lambda x: x[1], heapq.nsmallest(k, heap)[::-1])
