class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # 1. sort the balloons
        points.sort(key=lambda x: x[0])

        # 2. count the intervals of arrows
        arrow = 1
        cur_interval = points[0]
        for point in points:
            if cur_interval[1] < point[0]:
                arrow += 1
                cur_interval = point
            if cur_interval[0] <= point[0]:
                cur_interval[0] = point[0]
            if cur_interval[1] >= point[1]:
                cur_interval[1] = point[1]

        return arrow