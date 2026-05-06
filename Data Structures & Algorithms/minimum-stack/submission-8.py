class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val <= self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return 
