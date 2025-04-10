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

Case Methods


str.title() – Converts the first character of each word to uppercase.

str.swapcase() – Swaps the case of each character.



Searching & Indexing

str.find() – Returns the index of the first occurrence of a substring, or -1 if not found.

str.index() – Returns the index of the first occurrence of a substring, raises error if not found.

str.startswith() – Checks if the string starts with a specified value.

str.endswith() – Checks if the string ends with a specified value.

str.count() – Counts how many times a substring appears.



Replacing and Trimming

str.replace() – Replaces occurrences of a substring with another substring.

str.strip() – Removes leading and trailing whitespace.

str.lstrip() – Removes leading whitespace.

str.rstrip() – Removes trailing whitespace.



Splitting and Joining

str.split() – Splits the string into a list based on a separator.

str.join() – Joins elements of an iterable into a string.



String Checks

str.isalpha() – Checks if all characters are alphabetic.

str.isdigit() – Checks if all characters are digits.

str.isalnum() – Checks if all characters are alphanumeric.

str.isspace() – Checks if all characters are whitespace.

str.islower() – Checks if all characters are lowercase.

str.isupper() – Checks if all characters are uppercase.



Formatting and Encoding

str.format() – Formats strings using placeholders.

f-strings – Embeds expressions inside string literals using {}.

str.encode() – Encodes the string into bytes using a specific encoding.



Other

len() – Returns the number of characters in a string.


