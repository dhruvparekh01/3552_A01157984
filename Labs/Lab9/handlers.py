from abc import ABC, abstractmethod
from des import DesKey

from Labs.Lab9.crypto import CryptoMode, Request


class BaseHandler(ABC):
    """
    The abstract Handler class which is inherited by all the concrete Handlers.
    """

    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def handle_request(self, request: Request):
        pass

    def set_handle(self, handler):
        self.next_handler = handler


class ValidKeyHandler(BaseHandler):
    """
    Concrete Handler to validate the encryption key. Makes sure that the key is a multiple of 8.
    """

    def handle_request(self, request: Request):
        key = request.key

        if len(key) % 8 != 0:
            print('Invalid key')
            return
        else:
            self.next_handler.handle_request(request)


class FormatHandler(BaseHandler):
    """
    Concrete Handler to make sure the formats of the provided files is '.txt' as it is the only supported
    format.
    """

    def handle_request(self, request: Request):
        input_file = request.input_file
        output_file = request.output

        # validate both input and output files
        if self._valid_file(input_file) and self._valid_file(output_file):
            self.next_handler.handle_request(request)  # pass the control to the next handler
        else:
            print('Can only handle text files')

    @classmethod
    def _valid_file(cls, file) -> bool:
        """
        Private class method to validate if a file is valid or not.
        A file is valid if: (a) it is None, (b) It is a text file (c) it has the value 'print'
        :param file: to be validated
        """
        return file is None \
            or file[len(file) - 4:] == '.txt' \
            or file == 'print'


class EncodingHandler(BaseHandler):
    """
    Concrete Handler to convert all strings to byte-strings as it is the only supported format by the DES library.
    """

    def handle_request(self, request: Request):
        request.key = request.key.encode('UTF-8')  # convert the cipher key to byte string
        str_input = request.data_input

        if str_input is not None:  # If input is a string, encode it
            request.data_input = request.data_input.encode('UTF-8')
        else:
            with open(request.input_file, mode='rb') as file:
                message = file.read()

            request.data_input = message

        self.next_handler.handle_request(request)  # pass the control to the next handler


class EncryptHandler(BaseHandler):
    """
    Concrete Handler to encrypt/ decrypt data
    """

    def handle_request(self, request):
        key = DesKey(request.key)  # Create a DesKey object using the user provided key

        if request.encryption_state == CryptoMode.EN:
            request.result = key.encrypt(request.data_input, padding=True)
        else:
            request.result = key.decrypt(request.data_input, padding=True)

        self.next_handler.handle_request(request)  # pass the control to the next handler


class OutputHandler(BaseHandler):
    """
    Concrete handler to process and/or output the result
    """

    def handle_request(self, request):
        output_file_name = request.output

        # print the result
        if request.output == 'print':
            print(request.result)
            exit(0)

        # write the result to a file
        with open(output_file_name, mode='wb') as file:
            file.write(request.result)

        print('Process successfully completed!!')
