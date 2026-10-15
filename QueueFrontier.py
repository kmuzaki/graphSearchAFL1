class QueueFrontier:
    def __init__(self):
        self.queue = []

    def add(self, node):
        self.queue.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.queue)

    def empty(self):
        return len(self.queue) == 0

    def remove(self):
        if not self.empty():
            node = self.queue[0]
            self.queue = self.queue[1:]
            return node