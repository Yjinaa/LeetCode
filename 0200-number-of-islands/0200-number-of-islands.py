from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m,self.n = len(grid), len(grid[0])
        self.dxs = [0,1,0,-1]
        self.dys = [1,0,-1,0]
        visited = [[False]*self.n for _ in range(self.m)]
        queue = deque()
        islands = 0
        for i in range(self.m):
            for j in range(self.n):
                if visited[i][j] == False and grid[i][j]=="1":
                    self.bfs((i,j), visited, grid, queue)
                    islands += 1
        return islands

    def bfs(self, start, visited, grid, queue):
        queue.append(start)
        while queue:
            x,y = queue.popleft()
            visited[x][y] = True
            for dx, dy in zip(self.dxs, self.dys):
                nx, ny = x + dx, y + dy
                if 0<=nx<self.m and 0<=ny<self.n and not visited[nx][ny] and grid[nx][ny] == "1":
                    queue.append((nx,ny))
                    visited[nx][ny] = True

            