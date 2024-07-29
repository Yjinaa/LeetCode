class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        intervals.insert(left, newInterval)

        marged = []

        for interval in intervals:
            if not marged or marged[-1][1] < interval[0]:
                marged.append(interval)
            else:
                marged[-1][1] = max(marged[-1][1], interval[1])
    
        return marged
