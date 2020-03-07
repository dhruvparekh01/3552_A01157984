"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.read()

        for j in BookAnalyzer.COMMON_PUNCTUATION:
            self.text = self.text.replace(j, "")

        self.text = self.text.lower()
        words = set(self.text.split())

        self.text = words

    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        return list(self.text)


def main():
    book_analyzer = BookAnalyzer()

    for i in range(1000):
        book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("--------------------------------------------------")
    print(f"List of unique words (Count: {len(unique_words)})")
    print("--------------------------------------------------")
    for word in unique_words:
        print(word)
    print("--------------------------------------------------")


if __name__ == '__main__':
    main()
