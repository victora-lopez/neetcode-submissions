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
                if stack:
                    openBracket = stack.pop()
                    if bracketMap[bracket] == openBracket:
                        continue
                return False
        
        if stack:
            return False
        return True