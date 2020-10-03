# -------------------------------------------------------
#   Combination Sum - https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3481/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-10-02
# Project: leetcode-october-2020
# -------------------------------------------------------
class Solution:
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates,target,[],ret)
        return ret

    def dfs(self, candidates, target, path, ret):

        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return

        for i in range(len(candidates)):
            current = candidates[i]
            self.dfs(candidates[i:], target-current, path+[current], ret)


solution = Solution()
result = solution.combinationSum([2,3,6,7],7)
print(result)