from Labs.Lab8.catalogue_item import CatalogueItem


class Dvd(CatalogueItem):
    """
    Initialize Dvd
    """
    def __init__(self, release, reg_code, **kwargs):
        super().__init__(**kwargs)
        self._release = release
        self._reg_code = reg_code

    @property
    def release(self): return self._release

    @property
    def reg_code(self): return self._reg_code

    def __str__(self):
        return f"---- DVD: {self.title()}----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Release Date: {self.release}\n" \
               f"Registration Code: {self.reg_code}"
