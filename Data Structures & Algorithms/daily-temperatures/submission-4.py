class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # want to store as [temp, index] pair

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                distance = i - stackI
                res[stackI] = distance
            stack.append((t,i))
        return res