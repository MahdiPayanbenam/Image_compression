from ..helpers.frequency_analyzer import FrequencyAnalyzer
from ..tree_structure.huffman_tree import HuffmanTree
from .encoder import HuffmanEncoder
from .decoder import HuffmanDecoder

class HuffmanCompressor:
    """
    High-level interface for compressing and decompressing files.
    """
    @staticmethod
    def compress_file(input_file, output_file):
        """
        Compresses a text file using Huffman coding.
        """
        with open(input_file, "r") as file:
            text = file.read()

        frequencies = FrequencyAnalyzer.calculate_frequencies(text)
        huffman_tree = HuffmanTree(frequencies)
        codes = huffman_tree.generate_codes()
        encoded_text = HuffmanEncoder.encode_text(text, codes)
        HuffmanEncoder.save_to_file(encoded_text, codes, output_file)

    @staticmethod
    def decompress_file(input_file, output_file):
        """
        Decompresses a Huffman-encoded binary file.
        """
        HuffmanDecoder.decode_file(input_file, output_file)