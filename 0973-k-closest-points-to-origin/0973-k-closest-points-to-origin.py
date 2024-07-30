class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        d = {}
        for idx, point in enumerate(points):
            dist = self.get_distance(point)
            d[idx] = dist
        d = dict(sorted(d.items(), key=lambda x:x[1]))
        k_idx = [key for key in d.keys()][:k] 
        return [points[i] for i in k_idx]
    

    def get_distance(self, points):
        x1 = points[0]
        y1 = points[1]
        # x2 = points[1][0]
        # y2 = points[1][1]
        return sqrt((x1)**2 + (y1)**2)
        # return sqrt((x1-x2)**2 + (y1-y2)**2)