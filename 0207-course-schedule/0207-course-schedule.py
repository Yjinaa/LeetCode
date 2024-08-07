from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        visited = 0

        queue = deque([i for i in range(numCourses) if in_degree[i]==0])

        while queue:
            cur_course = queue.popleft()
            visited += 1
            for neighbor in graph[cur_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited == numCourses