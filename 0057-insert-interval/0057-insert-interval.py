class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        if not intervals:
            result.append(newInterval)
            return result
        #result.append(intervals[0])

        cur_interval = newInterval
        for i in range(len(intervals)):
            if intervals[i][1] < cur_interval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > cur_interval[1]:
                if i == 0 or intervals[i-1][0] <= cur_interval[1]:
                    result.append(cur_interval)
                result.append(intervals[i])
            else:
                cur_interval[0] = min(intervals[i][0], cur_interval[0])
                cur_interval[1] = max(intervals[i][1], cur_interval[1])
        
        if (not result) or result[-1][1] < cur_interval[1]:
            result.append(cur_interval)
        return result

