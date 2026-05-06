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
        operations:str = '+-*/'
        for c in tokens:
            stack.append(c)
            if stack[-1] in operations:
                stack.append(calc(stack.pop(),int(stack.pop()),int(stack.pop())))
        return int(stack.pop())