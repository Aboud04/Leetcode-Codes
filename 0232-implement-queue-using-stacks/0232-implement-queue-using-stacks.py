class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while True:
            if len(self.s1) == 1:
                tmp = self.s1.pop()
                break
            self.s2.append(self.s1.pop())

        while self.s2: self.s1.append(self.s2.pop())

        return tmp

    def peek(self) -> int:
        while True:
            if len(self.s1) == 1:
                tmp = self.s1.pop()
                self.s2.append(tmp)
                break
            self.s2.append(self.s1.pop())

        while self.s2: self.s1.append(self.s2.pop())

        return tmp

    def empty(self) -> bool:
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()