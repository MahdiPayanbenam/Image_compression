import tkinter as tk
from tkinter import filedialog, messagebox
from backend.compressor.huffman_compressor import HuffmanCompressor

class HuffmanUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Compression")
        self.root.geometry("400x200")
        self.root.resizable(False, False)  # Fix the window size

        # Title Label
        self.title_label = tk.Label(root, text="Huffman Compression Tool", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Compress Button
        self.compress_button = tk.Button(root, text="Compress File", command=self.compress_file, width=20)
        self.compress_button.pack(pady=5)

        # Decompress Button
        self.decompress_button = tk.Button(root, text="Decompress File", command=self.decompress_file, width=20)
        self.decompress_button.pack(pady=5)

    def compress_file(self):
        """Handles file selection and compression."""
        input_file = filedialog.askopenfilename(title="Select File to Compress")
        if not input_file:
            return

        output_file = filedialog.asksaveasfilename(title="Save Compressed File As", defaultextension=".bin")
        if not output_file:
            return

        try:
            HuffmanCompressor.compress_file(input_file, output_file)
            messagebox.showinfo("Success", "File successfully compressed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def decompress_file(self):
        """Handles file selection and decompression."""
        input_file = filedialog.askopenfilename(title="Select File to Decompress", filetypes=[("Binary Files", "*.bin")])
        if not input_file:
            return

        output_file = filedialog.asksaveasfilename(title="Save Decompressed File As", defaultextension=".txt")
        if not output_file:
            return

        try:
            HuffmanCompressor.decompress_file(input_file, output_file)
            messagebox.showinfo("Success", "File successfully decompressed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Run the UI
root = tk.Tk()
app = HuffmanUI(root)
root.mainloop()