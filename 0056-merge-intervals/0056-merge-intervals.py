class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        cur = 0
        for i in range(len(intervals)):
            if result == []:
                result.append(intervals[i])
            elif result[cur][1] < intervals[i][0]:
                cur += 1
                result.append(intervals[i])
            else:
                result[cur][1] = max(result[cur][1], intervals[i][1])
        return result