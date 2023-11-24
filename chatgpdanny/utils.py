import os

def read_object(file_name, store_path = 'store'):
    """Reads an object from a file, located in the store_path directory."""

    file_name = os.path.join(store_path, file_name)

    with open(file_name, 'r') as f:
        return f.read()