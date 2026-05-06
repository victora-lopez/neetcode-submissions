from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(operation:str,operand2:int,operand1:int) -> int:
            result:int = 0
            match operation:
                case '+':
                    result = operand1 + operand2
                case '-':
                    result = operand1 - operand2
                case '*':
                    result = operand1 * operand2
                case '/':
                    result = int(operand1/operand2)
            return result
        stack = []
        res:int = 0
        operations:list = ['+','-','*','/']
        tokens.reverse()
        for i in range(len(tokens)):
            stack.append(tokens.pop())
            if stack[-1] in operations:
                stack.append(calc(stack.pop(),int(stack.pop()),int(stack.pop())))
        return int(stack.pop())

# tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# solution = Solution()
# ans = solution.evalRPN(tokens);