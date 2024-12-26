class HuffmanNode:
    """
    Represents a node in the Huffman Tree.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None