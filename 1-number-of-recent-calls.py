# -------------------------------------------------------
# Number of Recent Calls - https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-10-01
# Project: leetcode-october-2020
# -------------------------------------------------------
class RecentCounter:

    def __init__(self):
        import collections
        self.queue = collections.deque()
        return

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)


recentCounter = RecentCounter()
recentCounter.ping(1)
recentCounter.ping(100)
recentCounter.ping(3001)
recentCounter.ping(3002)
recentCounter.ping(3003)
recentCounter.ping(3005)