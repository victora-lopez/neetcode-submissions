class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stack = []

        for bracket in s:
            if bracket in bracketMap.values():
                stack.append(bracket)
            else:
                if stack and bracketMap[bracket] == stack.pop():
                    continue
                return False
        
        return False if stack else True