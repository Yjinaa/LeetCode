from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        origin_color = image[sr][sc]
        queue = deque([(sr, sc)])
        m,n = len(image), len(image[0])
        visited = [[False]*n for _ in range(m)]
        visited[sr][sc] = True
        image[sr][sc] = color

        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0<= nc < n) and visited[nr][nc] != True and image[nr][nc] == origin_color:
                    image[nr][nc] = color
                    visited[nr][nc] = True
                    queue.append((nr,nc))

        return image

        