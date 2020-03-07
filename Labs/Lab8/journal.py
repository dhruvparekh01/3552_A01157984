from Labs.Lab8.catalogue_item import CatalogueItem


class Journal(CatalogueItem):
    """
      Represents a single journal in a library which is identified through
      it's call number.
      """

    def __init__(self, issue_no, pub, **kwargs):
        """
        :param call_num: a string
        :param name: a string
        :param num_copies: an int
        :param issue_no: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(**kwargs)
        self._issue_no = issue_no
        self._pub = pub

    def get_issue_no(self):
        """
        Getter for issue number
        :return: issue number of the journal object
        """
        return self._issue_no

    def get_pub(self):
        """
        Getter for publisher name
        :return: publisher name of the journal object
        """
        return self._pub

    def __str__(self):
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Issue No: {self._issue_no}\n" \
               f"Publisher: {self._pub}"
