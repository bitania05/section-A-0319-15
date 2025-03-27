README: Python String Methods (str.lower(), str.upper(), str.capitalize())

Introduction

This README provides documentation for three commonly used Python string methods:

str.lower()

str.upper()

str.capitalize()


These methods help manipulate the case of strings, making them useful for formatting text, processing user input, and ensuring consistency in string operations.


---

1. str.lower()

Description

The str.lower() method converts all uppercase letters in a string to lowercase.

Syntax

string.lower()

Example Usage

text = "Hello, WORLD!"
lowercase_text = text.lower()
print(lowercase_text)  # Output: "hello, world!"

How It Works

The method iterates through each character in the string.

If a character is uppercase (A-Z), it is converted to lowercase (a-z).

Non-alphabetical characters (numbers, symbols, spaces) remain unchanged.



---

2. str.upper()

Description

The str.upper() method converts all lowercase letters in a string to uppercase.

Syntax

string.upper()

Example Usage

text = "Hello, world!"
uppercase_text = text.upper()
print(uppercase_text)  # Output: "HELLO, WORLD!"

How It Works

The method scans each character in the string.

If the character is a lowercase letter (a-z), it is converted to uppercase (A-Z).

Non-alphabetical characters remain unchanged.



---

3. str.capitalize()

Description

The str.capitalize() method capitalizes the first character of a string and converts all other characters to lowercase.

Syntax

string.capitalize()

Example Usage

text = "hELLO, wORLD!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello, world!"

How It Works

The first character is converted to uppercase (if it’s a letter).

All remaining characters in the string are converted to lowercase.

If the first character is not a letter (e.g., a number or symbol), only the lowercase conversion applies.



---

Conclusion

These string methods are essential for handling text formatting in Python. They are widely used for data normalization, user input processing, and text-based operations.

