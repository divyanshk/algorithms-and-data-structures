#https://leetcode.com/contest/weekly-contest-93/problems/reordered-power-of-2/
class Solution:
    def reorderedPowerOf2(self, N):
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1 << i)) for i in range(32))
        
