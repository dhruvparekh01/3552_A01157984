from Labs.Lab2.catalogue_item import CatalogueItem


class Journal(CatalogueItem):
    def __init__(self, call_number, name, issue_no, pub, num_copies):
        super().__init__(num_copies, call_number)
        self._name = name
        self._issue_no = issue_no
        self._pub = pub
