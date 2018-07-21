#https://leetcode.com/problems/advantage-shuffle/description/
from collections import defaultdict

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]  
        """
        A_sorted = sorted(A)
        B_sorted = sorted(B)
        result = defaultdict(list)
        no_matches = []
        i = 0
        end = False
        for j in range(len(B)):
            if i == len(A):
                break
            while A_sorted[i] <= B_sorted[j]:
                no_matches.append(A_sorted[i])
                i += 1
                if i == len(A):
                    end = True
                    break
            if end:
                break
            result[B_sorted[j]].append(A_sorted[i])
            i += 1            
        return [result[elem].pop() if elem in result and result[elem] else no_matches.pop() for elem in B]
