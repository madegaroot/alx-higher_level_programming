#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""

def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("Can't add new attribute to this object")

 usage:
class SampleObject:
    def __init__(self, existing_attr):
        self.existing_attr = existing_attr

sample_instance = SampleObject("value")
print(sample_instance.__dict__)  # {'existing_attr': 'value'}

# Adding a new attribute
add_attribute(sample_instance, 'new_attr', 42)
print(sample_instance.__dict__)  # {'existing_attr': 'value', 'new_attr': 42}

# Trying to add a new attribute to an object that can't have new attributes
non_dict_object = 42
add_attribute(non_dict_object, 'new_attr', 42)  # Raises TypeError

