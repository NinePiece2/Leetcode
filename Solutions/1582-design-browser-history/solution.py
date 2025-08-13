class BrowserHistory:

    def __init__(self, homepage: str):
        self.stackA = []
        self.stackB = []
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.stackA.append(url)
        self.stackB.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.stackA) > 1:
            self.stackB.append(self.stackA.pop())
            steps -= 1
        return self.stackA[-1]

    def forward(self, steps: int) -> str:
        while steps and self.stackB:
            self.stackA.append(self.stackB.pop())
            steps -= 1
        return self.stackA[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
