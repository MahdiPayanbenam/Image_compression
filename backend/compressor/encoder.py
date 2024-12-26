class HuffmanEncoder:
    """
    Handles the encoding and saving of data using Huffman coding.
    """
    @staticmethod
    def encode_text(text, codes):
        """
        Encodes the text using the generated Huffman codes.
        """
        return ''.join(codes[char] for char in text)

    @staticmethod
    def save_to_file(encoded_text, codes, output_file):
        """
        Saves the encoded text and Huffman codes to a binary file.
        """
        with open(output_file, "wb") as file:
            # Save the Huffman codes (header)
            file.write((str(codes) + "\n").encode())

            # Save the encoded text as binary
            padding_length = 8 - len(encoded_text) % 8
            encoded_text += "0" * padding_length
            file.write(bytes([padding_length]))

            byte_array = bytearray()
            for i in range(0, len(encoded_text), 8):
                byte_array.append(int(encoded_text[i:i+8], 2))
            file.write(byte_array)