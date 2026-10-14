class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous = stack.pop()
                result[previous] = i - previous
            stack.append(i)
        return result
