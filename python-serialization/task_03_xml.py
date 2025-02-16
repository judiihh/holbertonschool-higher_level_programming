import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    :param dictionary: Dictionary to serialize
    :param filename: XML file to save data
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Error during serialization: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    :param filename: XML file to read from
    :return: Dictionary with deserialized XML data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        print("Error: XML file not found.")
        return None
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return None

# Example usage (uncomment to test)
# data = {"name": "Alice", "age": "25", "is_student": "True"}
# serialize_to_xml(data, "data.xml")
# loaded_data = deserialize_from_xml("data.xml")
# print(loaded_data)
