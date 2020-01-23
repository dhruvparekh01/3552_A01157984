import abc


class CatalogueItem(abc.ABC):
    def __init__(self, no_of_copies, index):
        self.no_of_copies = no_of_copies
        self.index = index
