import json

from Labs.Lab5.dict_enum import FileExtensions


class FileHandler:

    @staticmethod
    def load_data(path, file_extension):
        if file_extension not in [FileExtensions.Json, FileExtensions.Txt]:
            raise InvalidFileTypeError(file_extension)

        with open(path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    @staticmethod
    def write_lines(path, lines):
        with open(path, mode='a', encoding='utf-8') as file:
            file.writelines(lines)


class InvalidFileTypeError(Exception):
    def __init__(self, extension):
        print(extension, "is not supported")
