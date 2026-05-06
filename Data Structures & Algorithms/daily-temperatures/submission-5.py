# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
#
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on
# a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i]
# to 0 instead.
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            elif temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    ans_index = stack.pop()
                    ans[ans_index] = i - ans_index
                stack.append(i)
        return ans



# temperatures = [30,38,30,36,35,40,28]
# [1,4,1,2,1,0,0]
# solution = Solution()
# ans = solution.dailyTemperatures(temperatures)