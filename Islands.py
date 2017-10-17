# Problem: https://leetcode.com/problems/number-of-islands/description/
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # visited list
        visited = [[False]*len(grid[0]) for _ in xrange(len(grid))]
        
        queue = []
        numIslands = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                # found land and it is unvisited
                if grid[i][j] == '1' and visited[i][j] == False:
                    # traverse this island
                    numIslands += 1
                    queue.append((i, j))
                    visited[i][j] = True

                    while queue:
                        # pop the first item in the queue
                        x, y = queue.pop(0)

                        # check for neighbors
                        if x+1 < len(grid) and grid[x+1][y] == '1' and visited[x+1][y] == False:
                            queue.append((x+1, y))
                            visited[x+1][y] = True
                        if x-1 >= 0 and grid[x-1][y] == '1' and visited[x-1][y] == False:
                            queue.append((x-1, y))
                            visited[x-1][y] = True
                        if y+1 < len(grid[0]) and grid[x][y+1] == '1' and visited[x][y+1] == False:
                            queue.append((x, y+1))
                            visited[x][y+1] = True
                        if y-1 >= 0 and grid[x][y-1] == '1' and visited[x][y-1] == False:
                            queue.append((x, y-1))
                            visited[x][y-1] = True
        return numIslands
