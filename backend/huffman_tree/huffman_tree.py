from helpers.priority_queue import PriorityQueue

class HuffmanNode:
    """
    Represents a node in the Huffman Tree.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanTree:
    """
    Manages the construction of the Huffman Tree and code generation.
    """
    def __init__(self, frequencies):
        self.frequencies = frequencies
        self.root = self.build_tree()

    def build_tree(self):
        """
        Builds the Huffman Tree from character frequencies.
        """
        priority_queue = PriorityQueue()
        for char, freq in self.frequencies.items():
            priority_queue.insert(HuffmanNode(char, freq))

        while len(priority_queue) > 1:
            left = priority_queue.pop()
            right = priority_queue.pop()
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            priority_queue.insert(merged)

        return priority_queue.pop()