import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    :param data: Dictionary to serialize
    :param filename: JSON file to save data
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    :param filename: JSON file to read from
    :return: Dictionary with deserialized JSON data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Example usage (uncomment to test)
# data = {"name": "Alice", "age": 25, "city": "New York"}
# serialize_and_save_to_file(data, "data.json")
# loaded_data = load_and_deserialize("data.json")
# print(loaded_data)
