1. keys()

Returns a view object of all the keys in the dictionary.


1. values()

Returns a view object of all the values in the dictionary.



1. items()

Returns a view object of all key-value pairs as tuples.


1. get(key, default)

Returns the value for a key if it exists; otherwise returns the default value if provided (or None if not).

Safe way to access values without raising a KeyError.



1. pop(key)

Removes the specified key from the dictionary and returns its value.

If the key doesn’t exist, it raises a KeyError (unless a default value is given).

# Define a dictionary
student = {
    'name': 'John',
    'age': 21,
    'major': 'Computer Science'
}

# keys(): Returns a list of keys
print("Keys:", list(student.keys()))

# values(): Returns a list of values
print("Values:", list(student.values()))

# items(): Returns a list of key-value pairs
print("Items:", list(student.items()))

# get(): Returns the value for a specified key
print("Name:", student.get('name'))

# pop(): Removes the specified key and returns its value
age = student.pop('age')
print("Popped Age:", age)

# Final state of dictionary
print("Updated Dictionary:", student)