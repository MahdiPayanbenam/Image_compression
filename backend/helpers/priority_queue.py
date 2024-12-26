class PriorityQueue:
    """
    Priority queue implementation for managing Huffman nodes.
    """
    def __init__(self):
        self.queue = []

    def insert(self, node):
        self.queue.append(node)
        self.queue.sort(key=lambda x: x.freq)

    def pop(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)