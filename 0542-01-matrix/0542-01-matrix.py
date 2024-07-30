from collections import deque
import sys
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:   
        m, n = len(mat), len(mat[0]) 
        dist = [[sys.maxsize] * n for _ in range(m)]
        queue = deque()
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    dist[i][j] = 0
        
        while queue:
            x, y = queue.popleft()
            for dir in dirs:
                nx, ny = x + dir[0], y + dir[1]
                if 0 <= nx < m and 0 <= ny < n:
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))

        return dist
        



