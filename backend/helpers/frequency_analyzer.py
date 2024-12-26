class FrequencyAnalyzer:
    """
    This class handles frequency analysis for a given text.
    """
    @staticmethod
    def calculate_frequencies(text):
        frequencies = {}
        for char in text:
            frequencies[char] = frequencies.get(char, 0) + 1
        return frequencies