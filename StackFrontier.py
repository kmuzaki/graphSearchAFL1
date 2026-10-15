class StackFrontier:
    def __init__(self):
        self.stack = []

    def add(self, node):
        self.stack.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.stack)

    def empty(self):
        return len(self.stack) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.stack[-1]
            self.stack.pop()
            return node