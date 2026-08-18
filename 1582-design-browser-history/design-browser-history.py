class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        # Delete all forward history
        self.history = self.history[:self.current + 1]

        # Add new URL
        self.history.append(url)

        # Move to the new page
        self.current += 1

    def back(self, steps):
        # Move backward, but not before index 0
        self.current = max(0, self.current - steps)

        return self.history[self.current]

    def forward(self, steps):
        # Move forward, but not beyond the last page
        self.current = min(len(self.history) - 1, self.current + steps)

        return self.history[self.current]