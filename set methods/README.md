
1. add()
Use: To insert a single new element into a set.
When: You want to expand your set one item at a time.

fruits = {"apple", "banana"}
fruits.add("orange")  # Adds 'orange' to the set


---

2. copy()

Use: To create a shallow copy of a set.
When: You need to work with or modify a duplicate set without affecting the original.

original = {1, 2, 3}
backup = original.copy()
backup.add(4)
# original remains unchanged


---

3. clear()

Use: To remove all items from a set.
When: You want to reset or empty the set completely.

data = {10, 20, 30}
data.clear()
# data is now an empty set: set()


---

4. difference(*others)

Use: To get elements in the first set that are not in the others.
When: You want to filter out common elements from another set or multiple sets.

5. difference_update(others) method works in Python:


---

Purpose:

difference_update() removes elements from the original set that are present in the other set(s). It modifies the original set in place and returns None.

6. discard(elem) :


---

Purpose:

discard(elem) removes the element from the set if it exists.
Unlike remove(), it won’t raise an error if the element is not found.

7. intersection(*others)

Use: Returns a new set containing elements common to all sets.

8. intersection(*others)

Use: Returns a new set containing elements common to all sets.

Key Difference:

intersection() returns a new set.

intersection_update() modifies the original set.