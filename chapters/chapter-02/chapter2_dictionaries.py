# Chapter 2.2: Dictionaries
# Python vs C# Dictionary Operations

"""
C# Dictionary Operations:
Dictionary<string, int> ages = new Dictionary<string, int>();
ages["Alice"] = 25;
ages["Bob"] = 30;
ages.Add("Charlie", 35);
int aliceAge = ages["Alice"];
bool hasKey = ages.ContainsKey("Alice");
"""

from typing import Any, Dict

# Python Dictionaries - Key-value pairs (like C# Dictionary<K,V>)
ages: Dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}  # Dictionary literal
print(f"Ages dictionary: {ages}")
print(f"Type: {type(ages)}")

# Accessing values (same as C#)
alice_age = ages["Alice"]  # Get value by key
print(f"Alice's age: {alice_age}")

# Adding/updating values (same as C#)
ages["David"] = 28  # Add new key-value pair
ages["Alice"] = 26  # Update existing value
print(f"After updates: {ages}")

# Safe access with get() method (better than C# TryGetValue)
eve_age = ages.get("Eve", 0)  # Returns 0 if key doesn't exist
print(f"Eve's age (with default): {eve_age}")

frank_age = ages.get("Frank")  # Returns None if key doesn't exist
print(f"Frank's age (no default): {frank_age}")

# Checking if key exists (like C# ContainsKey)
has_alice = "Alice" in ages
has_zoe = "Zoe" in ages
print(f"Has Alice: {has_alice}")
print(f"Has Zoe: {has_zoe}")

# Dictionary methods
print(f"\nDictionary methods:")
print(f"Keys: {list(ages.keys())}")  # Like C# Keys property
print(f"Values: {list(ages.values())}")  # Like C# Values property
print(f"Items: {list(ages.items())}")  # Key-value pairs as tuples

# Removing elements
removed_age = ages.pop("Charlie", None)  # Remove and return value
print(f"Removed Charlie's age: {removed_age}")
print(f"After removal: {ages}")

# Dictionary length
length = len(ages)
print(f"Dictionary length: {length}")

# Iterating over dictionaries (different patterns than C#)
print(f"\nIteration patterns:")

# Iterate over keys (default behavior)
print("Keys only:")
for name in ages:
    print(f"  {name}")

# Iterate over values
print("Values only:")
for age in ages.values():
    print(f"  {age}")

# Iterate over key-value pairs (like C# foreach with KeyValuePair)
print("Key-value pairs:")
for name, age in ages.items():
    print(f"  {name}: {age}")

# Dictionary comprehensions (like LINQ in C#)
# Create dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dictionary: {squares}")

# Filter and transform existing dictionary
adults = {name: age for name, age in ages.items() if age >= 18}
print(f"Adults only: {adults}")

# Uppercase names
upper_ages = {name.upper(): age for name, age in ages.items()}
print(f"Uppercase names: {upper_ages}")

# Nested dictionaries (like C# Dictionary<string, Dictionary<string, object>>)
employees: Dict[str, Dict[str, object]] = {
    "emp001": {
        "name": "Alice Johnson",
        "department": "Engineering",
        "salary": 75000,
        "active": True,
    },
    "emp002": {
        "name": "Bob Smith",
        "department": "Marketing",
        "salary": 65000,
        "active": True,
    },
    "emp003": {
        "name": "Charlie Brown",
        "department": "Engineering",
        "salary": 80000,
        "active": False,
    },
}

print(f"\nEmployees database:")
for emp_id, emp_data in employees.items():
    print(f"  {emp_id}: {emp_data['name']} - {emp_data['department']}")

# Accessing nested values
alice_salary = employees["emp001"]["salary"]
print(f"Alice's salary: ${alice_salary:,}")

# Safe nested access with get()
nonexistent_dept = employees.get("emp999", {}).get("department", "Unknown")
print(f"Non-existent employee department: {nonexistent_dept}")

# Updating nested dictionaries
employees["emp001"]["salary"] = 78000  # Give Alice a raise
employees["emp001"]["last_review"] = "2024-08-01"  # Add new field
print(f"Alice after update: {employees['emp001']}")

# Dictionary methods for merging (Python 3.9+)
personal_info: Dict[str, Dict[str, Any]] = {"emp001": {"age": 28, "city": "Seattle"}}
# Merge dictionaries (like C# dictionary assignment)
for emp_id in personal_info:
    if emp_id in employees:
        employees[emp_id].update(personal_info[emp_id])

print(f"Alice with personal info: {employees['emp001']}")

# Default dictionaries concept (collections.defaultdict equivalent)
from collections import defaultdict

# Count occurrences of letters
letter_count: defaultdict[str, int] = defaultdict(int)  # Default value is 0 for new keys
text = "hello world"
for char in text:
    if char.isalpha():
        letter_count[char] += 1

print(f"\nLetter counts: {dict(letter_count)}")

# Group items by category
from collections import defaultdict

items_by_category: defaultdict[str, list[str]] = defaultdict(list)  # Default value is empty list
items = [
    ("apple", "fruit"),
    ("carrot", "vegetable"),
    ("banana", "fruit"),
    ("spinach", "vegetable"),
    ("orange", "fruit"),
]

for item, category in items:
    items_by_category[category].append(item)

print(f"Items by category: {dict(items_by_category)}")

# Dictionary vs list performance comparison
print(f"\nPerformance comparison:")
print("Dictionary lookup: O(1) average case")
print("List search: O(n) average case")

# Practical example: Phone book
phone_book = {"Alice": "555-0123", "Bob": "555-0124", "Charlie": "555-0125"}


def lookup_phone(name: str) -> str:
    """Look up phone number by name."""
    return phone_book.get(name, "Number not found")


print(f"\nPhone book lookup:")
print(f"Alice: {lookup_phone('Alice')}")
print(f"David: {lookup_phone('David')}")


# Reverse lookup (value to key)
def reverse_lookup_phone(number: str) -> str:
    """Find name by phone number."""
    for name, phone in phone_book.items():
        if phone == number:
            return name
    return "Name not found"


print(f"Reverse lookup 555-0124: {reverse_lookup_phone('555-0124')}")

# Dictionary copying (important!)
original_dict = {"a": 1, "b": 2}
reference = original_dict  # Reference, not copy!
shallow_copy = original_dict.copy()  # Shallow copy
import copy

deep_copy = copy.deepcopy(original_dict)  # Deep copy

original_dict["c"] = 3
print(f"\nCopying behavior:")
print(f"Original: {original_dict}")
print(f"Reference: {reference}")  # Changed!
print(f"Shallow copy: {shallow_copy}")  # Unchanged
print(f"Deep copy: {deep_copy}")  # Unchanged

# Dictionary with different value types (like C# Dictionary<string, object>)
mixed_data: Dict[str, object] = {
    "name": "Alice",
    "age": 25,
    "scores": [95, 87, 92],
    "active": True,
    "metadata": {"created": "2024-01-01", "updated": "2024-08-01"},
}

print(f"\nMixed data dictionary:")
for key, value in mixed_data.items():
    print(f"  {key}: {value} ({type(value).__name__})")

"""
Key differences from C#:
1. Dictionary literal syntax: {"key": value}
2. No need to specify types
3. get() method for safe access with defaults
4. Dictionary comprehensions
5. items(), keys(), values() methods return views
6. Can use 'in' operator to check key existence
7. Can hold mixed value types
8. More flexible iteration patterns
9. defaultdict for automatic default values
"""
