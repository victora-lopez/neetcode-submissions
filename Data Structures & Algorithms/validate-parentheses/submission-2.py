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
                    if bracketMap[bracket] != openBracket:
                        return False
                else:
                    return False
        
        if stack:
            return False
        return True