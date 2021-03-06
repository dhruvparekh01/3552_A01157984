from Labs.Lab2.catalogue_item import CatalogueItem


class Dvd(CatalogueItem):
    """
    Initialize Dvd
    """
    def __init__(self, call_number, release, reg_code, num_copies, title):
        super().__init__(num_copies, call_number, title)
        self._release = release
        self._reg_code = reg_code

    def get_release(self):
        """
        Getter for release date
        :return: release date of the object
        """
        return self._release

    def get_reg_code(self):
        """
        Getter for registration code
        :return: registration code of the object
        """
        return self._reg_code

    def __str__(self):
        return f"---- DVD: {self.get_title()}----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.no_of_copies}\n" \
               f"Release Date: {self._release}\n" \
               f"Registration Code: {self._reg_code}"
