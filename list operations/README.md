append(): Adds an element to the end of the list. 
insert(): Inserts an element at a specified index. 
remove(): Removes the first occurrence of a value.
 pop(): Removes the element at the given position in the list, or the last element if no index is specified. 
len(): Returns the length of the list. 
sort(): Sorts the list in ascending order. 
Slicing: Accessing sub-parts of a list

# Starting list
fruits = ['apple', 'banana', 'cherry']

# append(): Add element at the end
fruits.append('orange')
print("After append:", fruits)

# insert(): Add element at a specific index
fruits.insert(1, 'kiwi')
print("After insert at index 1:", fruits)

# remove(): Remove first occurrence of a value
fruits.remove('banana')
print("After remove 'banana':", fruits)

# pop(): Remove element at specific index (or last by default)
popped_item = fruits.pop(2)
print("After pop at index 2:", fruits)
print("Popped item:", popped_item)

# len(): Get the number of elements in the list
print("Length of list:", len(fruits))

# sort(): Sort list in ascending order
fruits.sort()
print("Sorted list:", fruits)

# slicing: Get a sublist (from index 1 to 2)
sublist = fruits[1:3]
print("Sliced sublist (index 1 to 2):", sublist)