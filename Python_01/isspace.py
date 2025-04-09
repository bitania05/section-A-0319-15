

text1 = "   "
text2 = "\n\t "
text3 = " hello "
text4 = ""

print(text1.isspace())  # True – only spaces
print(text2.isspace())  # True – newline, tab, space
print(text3.isspace())  # False – has letters
print(text4.isspace())  # False – empty string