
# Sample strings
s1 = "Hello"
s2 = "12345"
s3 = "Hello123"
s4 = "Hello 123"
s5 = ""


# isalnum() returns True if all characters are alphanumeric (letters and numbers)
print(s3.isalnum())  # True
print(s4.isalnum())  # False (contains space)
print(s5.isalnum())  # False (empty string)
