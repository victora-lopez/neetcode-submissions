class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }

        stack = []

        for bracket in s:
            if bracket in bracketMap.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                lastBracket = stack.pop()
                if bracket != bracketMap[lastBracket]:
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True