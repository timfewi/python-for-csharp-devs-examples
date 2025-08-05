# Chapter 2.3: Tuples and Sets
# Python vs C# Tuple and HashSet Operations

"""
C# Tuple and HashSet Operations:
(string, int) person = ("Alice", 25);
var (name, age) = person;
HashSet<string> uniqueNames = new HashSet<string> {"Alice", "Bob", "Alice"};
bool added = uniqueNames.Add("Charlie");
"""

# ===== TUPLES =====
# Python Tuples - Immutable sequences (like C# ValueTuple)
person = ("Alice", 25, "Engineer")  # Tuple literal
print(f"Person tuple: {person}")
print(f"Type: {type(person)}")

# Accessing tuple elements (same as lists, but immutable)
name = person[0]
age = person[1]
job = person[2]
print(f"Name: {name}, Age: {age}, Job: {job}")

# Tuple unpacking (like C# deconstruction)
name, age, job = person  # Unpack all values
print(f"Unpacked - Name: {name}, Age: {age}, Job: {job}")

# Partial unpacking with underscore (ignore values)
name, _, job = person  # Ignore age
print(f"Partial unpack - Name: {name}, Job: {job}")

# Named tuples (like C# record types)
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "job"])
alice = Person("Alice", 25, "Engineer")
print(f"\nNamed tuple: {alice}")
print(f"Name: {alice.name}")  # Access by name instead of index
print(f"Age: {alice.age}")
print(f"Job: {alice.job}")

# Named tuples are still tuples
name, age, job = alice  # Can still unpack
print(f"Unpacked named tuple: {name}, {age}, {job}")

# Tuples are immutable (unlike lists)
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# This would cause an error:
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# But you can create a new tuple
new_coordinates = (15, 20)
print(f"New coordinates: {new_coordinates}")

# Tuple methods (limited because they're immutable)
numbers = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = numbers.count(2)  # Count occurrences
index_of_3 = numbers.index(3)  # Find first index
print(f"Numbers: {numbers}")
print(f"Count of 2: {count_of_2}")
print(f"Index of 3: {index_of_3}")

# Single element tuple (note the comma!)
single = (42,)  # Comma is required to make it a tuple
not_tuple = 42  # This is just parentheses around an integer
print(f"Single element tuple: {single}, type: {type(single)}")
print(f"Not a tuple: {not_tuple}, type: {type(not_tuple)}")

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}, length: {len(empty)}")


# Tuples as function return values (common pattern)
def get_user_info(user_id: int) -> tuple[str, int, str]:
    """Return user information as a tuple."""
    # Simulate database lookup
    return ("John Doe", 30, "john@example.com")


user_name, user_age, user_email = get_user_info(123)
print(f"\nUser info: {user_name}, {user_age}, {user_email}")

# Tuples in dictionaries (immutable keys)
locations = {(0, 0): "Origin", (10, 20): "Point A", (-5, 15): "Point B"}
print(f"Locations: {locations}")
print(f"Location at (10, 20): {locations[(10, 20)]}")

# ===== SETS =====
# Python Sets - Unique collections (like C# HashSet<T>)
unique_names = {"Alice", "Bob", "Charlie", "Alice"}  # Duplicates removed
print(f"\nUnique names set: {unique_names}")
print(f"Type: {type(unique_names)}")

# Creating sets from lists (removes duplicates)
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_list)
print(f"Numbers list: {numbers_list}")
print(f"Unique numbers set: {unique_numbers}")

# Adding elements (like C# HashSet.Add)
unique_names.add("David")  # Add single element
print(f"After adding David: {unique_names}")

unique_names.add("Alice")  # Adding duplicate has no effect
print(f"After adding Alice again: {unique_names}")

# Removing elements
unique_names.remove("Bob")  # Remove element (raises error if not found)
print(f"After removing Bob: {unique_names}")

unique_names.discard("Zoe")  # Remove element (no error if not found)
print(f"After discarding Zoe (not in set): {unique_names}")

# Checking membership (like C# HashSet.Contains)
has_alice = "Alice" in unique_names
has_bob = "Bob" in unique_names
print(f"Has Alice: {has_alice}")
print(f"Has Bob: {has_bob}")

# Set operations (mathematical set operations)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet operations:")
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union (elements in either set)
union = set1 | set2  # or set1.union(set2)
print(f"Union (|): {union}")

# Intersection (elements in both sets)
intersection = set1 & set2  # or set1.intersection(set2)
print(f"Intersection (&): {intersection}")

# Difference (elements in set1 but not set2)
difference = set1 - set2  # or set1.difference(set2)
print(f"Difference (-): {difference}")

# Symmetric difference (elements in either set, but not both)
symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print(f"Symmetric difference (^): {symmetric_diff}")

# Set comprehensions (like dictionary comprehensions)
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"\nEven squares set: {even_squares}")

# Practical example: Finding unique words
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()
unique_words = set(words)
print(f"\nText: {text}")
print(f"All words: {words}")
print(f"Unique words: {unique_words}")
print(f"Word count: {len(words)}")
print(f"Unique word count: {len(unique_words)}")

# Converting between sets and lists
unique_list = list(unique_words)  # Convert set to list
print(f"Unique words as list: {unique_list}")

# Frozenset (immutable set, like C# ImmutableHashSet)
immutable_set = frozenset([1, 2, 3, 4])
print(f"\nFrozen set: {immutable_set}")
# immutable_set.add(5)  # This would cause an error

# Frozensets can be used as dictionary keys (since they're immutable)
set_dict = {frozenset([1, 2]): "Pair A", frozenset([3, 4]): "Pair B"}
print(f"Dictionary with frozenset keys: {set_dict}")

# Performance comparison
print(f"\nPerformance characteristics:")
print("Set membership check: O(1) average case")
print("List membership check: O(n) average case")


# Practical example: Remove duplicates while preserving order
def remove_duplicates_preserve_order(items: list) -> list:
    """Remove duplicates from list while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


original = [1, 2, 3, 2, 4, 3, 5, 1]
deduplicated = remove_duplicates_preserve_order(original)
print(f"\nOriginal: {original}")
print(f"Deduplicated (order preserved): {deduplicated}")
print(f"Using set() (order not preserved): {list(set(original))}")

# When to use each collection type
print(f"\nWhen to use each type:")
print("List: Ordered, mutable, allows duplicates")
print("Tuple: Ordered, immutable, allows duplicates")
print("Set: Unordered, mutable, no duplicates")
print("Frozenset: Unordered, immutable, no duplicates")

"""
Key differences from C#:
TUPLES:
1. Immutable sequences (like C# ValueTuple)
2. Can unpack into multiple variables
3. Named tuples provide structure without full class
4. Single element requires comma: (item,)
5. Can be used as dictionary keys (immutable)

SETS:
1. Mathematical set operations (|, &, -, ^)
2. Set comprehensions
3. Fast membership testing O(1)
4. No indexing (unordered)
5. Frozenset for immutable version
6. No duplicates automatically
"""
