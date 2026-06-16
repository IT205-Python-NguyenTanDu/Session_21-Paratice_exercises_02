class InvalidQuantityError(ValueError):
    """Raised when an order quantity is zero or negative."""


class ItemNotFoundError(KeyError):
    """Raised when a drink code does not exist in the menu."""
