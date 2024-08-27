import sys
class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []
        self.min_val = sys.maxsize
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if val <= self.min_val:
            self.min_val = val
            self.min_s.append(self.min_val)

    def pop(self) -> None:
        if len(self.s) == 0:
            return None
        else:
            top = self.top()
            self.s = self.s[:-1]
            if top == self.min_val:
                self.min_s = self.min_s[:-1]
                if len(self.min_s) != 0:
                    self.min_val = self.min_s[-1]
                else:
                    self.min_val = sys.maxsize
            return top

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min_s[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()