# -------------------------------------------------------
# Remove Covered Intervals - https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3483/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-10-04
# Project: leetcode-october-2020
# -------------------------------------------------------
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[0],-x[1]))
        print(intervals)
        last = -1
        count = 0
        for i in intervals:
            if last < i[1]:
                count +=1
                last = i[1]
        return count
#[[3,10],[4,10],[5,11]]
#[[1,4],[3,6],[2,8]] -> 2
#[[0,10],[5,12]] - 2
solution = Solution()
result = solution.removeCoveredIntervals([[3,10],[4,10],[5,11]])
print(result)