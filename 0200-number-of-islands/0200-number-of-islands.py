from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m,self.n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        islands = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]=="1":
                    self.bfs((i,j), grid, directions)
                    islands += 1
        return islands

    def bfs(self, start, grid, directions):
        queue = deque()
        queue.append(start)
        grid[start[0]][start[1]] = "0"
        while queue:
            x,y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<=nx<self.m and 0<=ny<self.n and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    queue.append((nx,ny))
            