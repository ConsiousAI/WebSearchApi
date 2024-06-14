class APIError(Exception):
    """Exception raised for errors in the API response."""
    pass

class InvalidQueryError(Exception):
    """Exception raised for invalid queries."""
    pass
