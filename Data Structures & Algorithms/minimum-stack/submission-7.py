class MinStack:

    def __init__(self):
        self.minStack = []
        self.orderStack = []

    def push(self, val: int) -> None:
        self.orderStack.append(val)
        if self.minStack and val > self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.orderStack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.orderStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
