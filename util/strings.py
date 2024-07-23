"""
------------------------------------------
---- Helper string classes, functions ----
------------------------------------------
"""

def to_str(bytes_or_str):
    """Takes a bytes or str and always returns a str"""
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str):
    """Takes a bytes or str and always returns a bytes"""
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value