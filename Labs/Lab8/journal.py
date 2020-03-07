from Labs.Lab8.catalogue_item import CatalogueItem


class Journal(CatalogueItem):
    """
      Represents a single journal in a library which is identified through
      it's call number.
      """

    def __init__(self, issue_no, pub, **kwargs):
        """
        :param issue_no: an int
        :param pub: a string
        :param **kwargs: See below

        :keyword Arguments:
            * *call_num* (```str```)
            * *title* (```str```)
            * *num_copies* (```int```)

        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(**kwargs)
        self._issue_no = issue_no
        self._pub = pub

    @property
    def issue_no(self): return self._issue_no

    def pub(self): return self._pub

    def __str__(self):
        return f"---- Journal: {self.title} ----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Issue No: {self._issue_no}\n" \
               f"Publisher: {self._pub}"
