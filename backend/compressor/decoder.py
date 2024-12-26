class HuffmanDecoder:
    """
    Handles the decoding of Huffman-encoded files.
    """
    @staticmethod
    def decode_file(input_file, output_file):
        """
        Decodes a Huffman-encoded binary file and saves the result.
        """
        with open(input_file, "rb") as file:
            # Read the Huffman codes (header)
            codes = eval(file.readline().decode().strip())
            reverse_codes = {v: k for k, v in codes.items()}

            # Read the binary data
            padding_length = file.read(1)[0]
            byte_array = file.read()

            binary_string = ''.join(format(byte, "08b") for byte in byte_array)
            binary_string = binary_string[:-padding_length]

            # Decode the binary string
            decoded_text = ""
            current_code = ""
            for bit in binary_string:
                current_code += bit
                if current_code in reverse_codes:
                    decoded_text += reverse_codes[current_code]
                    current_code = ""

            # Write the decoded text to the output file
            with open(output_file, "w") as output:
                output.write(decoded_text)