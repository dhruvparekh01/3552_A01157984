class NegativeBalanceException(Exception):
    """
    Custom exception raised when the user ties to take more money out of his account than there is.
    """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
