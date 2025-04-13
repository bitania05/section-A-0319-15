set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
set3 = {0, 2, 3, 9}

set1.intersection_update(set2, set3)

print(set1)  # Output: {2, 3}