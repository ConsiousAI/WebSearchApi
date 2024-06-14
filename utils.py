def validate_query(query):
    if isinstance(query, str) and query.strip():
        return True
    return False
