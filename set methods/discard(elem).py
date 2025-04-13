my_set = {1, 2, 3, 4}

# Discard an existing element
my_set.discard(3)

# Discard a non-existing element (no error)
my_set.discard(10)

print(my_set)  # Output: {1, 2, 4}