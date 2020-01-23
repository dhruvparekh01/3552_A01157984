from Labs.Lab2.catalogue_item import CatalogueItem


class Dvd(CatalogueItem):
    def __init__(self, call_number, release, reg_code, num_copies):
        super().__init__(num_copies, call_number)
        self._release = release
        self._reg_code = reg_code

