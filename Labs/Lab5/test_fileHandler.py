from unittest import TestCase

from Labs.Lab5.dict_enum import FileExtensions
from Labs.Lab5.file_handler import FileHandler


class TestFileHandler(TestCase):
    def test_load_data(self):
        data = FileHandler.load_data('data.json', FileExtensions.Json)
        self.assertIsNotNone(data)

    def test_write_lines(self):
        lines = 'Hello world'
        path = 'test.txt'
        FileHandler.write_lines(path, lines)

        with open(path, mode='r') as test_file:
            data = test_file.read()
            self.assertIsNotNone(data)
