from Labs.Lab5.dict_enum import FileExtensions
from Labs.Lab5.file_handler import FileHandler
import difflib


class Dictionary:
    def __init__(self):
        self.dict = {}

    def load_dictionary(self, filepath):
        try:
            self.dict = FileHandler.load_data(filepath, FileExtensions.Json)
        except FileNotFoundError:
            print('Invalid file path')
        except:
            print('Unknown exception occurred')

    def query_definition(self, word):
        word = word.lower()
        found = self.dict.get(word)
        if found is None:
            close_matches = difflib.get_close_matches(word, self.dict.keys())
            return f'Match not Found.\nInstead try: {close_matches}'
        else:
            found_str = Dictionary.get_as_str(found)
            FileHandler.write_lines('Queries.txt', word + ': ' + found_str+'\n')
            return found_str

    @staticmethod
    def get_as_str(lst):
        s = ''
        for i in lst:
            s += i + '\n'

        return s


class DictNotLoadedException(Exception):
    pass


if __name__ == '__main__':
    file = 'data.txt'
    d1 = Dictionary()
    d1.load_dictionary(file)
    word = ''

    while True:
        word = input('Enter a word to query or enter "exitprogram" to quit\n')
        if word == 'exitprogram':
            break
        print(d1.query_definition(word))
