class MinStack:

    def __init__(self):
        self.minstack = []
        self.order = []

    def push(self, val: int) -> None:
        self.order.append(val)
        if not self.minstack or self.minstack[-1] > val:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.order.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.order[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
