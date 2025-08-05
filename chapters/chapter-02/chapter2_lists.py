# Chapter 2.1: Lists
# Python vs C# List/Array Operations

"""
C# List and Array Operations:
List<string> names = new List<string> {"Alice", "Bob", "Charlie"};
string[] fixedArray = {"Alice", "Bob", "Charlie"};
names.Add("David");
names.Remove("Bob");
string first = names[0];
int count = names.Count;
"""

# Python Lists - Dynamic arrays that can hold any type!
names = ["Alice", "Bob", "Charlie"]  # No type declaration needed
print(f"Initial list: {names}")
print(f"Type: {type(names)}")

# Adding elements (similar to C# List.Add)
names.append("David")  # Add to end (like C#'s Add)
print(f"After append: {names}")

names.insert(1, "Eve")  # Insert at specific index (like C#'s Insert)
print(f"After insert at index 1: {names}")

# Removing elements (similar to C# List.Remove)
names.remove("Bob")  # Remove first occurrence (like C#'s Remove)
print(f"After remove 'Bob': {names}")

removed = names.pop()  # Remove and return last element (no direct C# equivalent)
print(f"Popped element: {removed}")
print(f"After pop: {names}")

removed_at_index = names.pop(1)  # Remove at specific index (like C#'s RemoveAt)
print(f"Popped at index 1: {removed_at_index}")
print(f"After pop at index: {names}")

# Accessing elements (same as C#)
first_name = names[0]  # First element
last_name = names[-1]  # Last element (Python-specific negative indexing!)
print(f"First: {first_name}, Last: {last_name}")

# List slicing (very different from C#!)
full_list = ["A", "B", "C", "D", "E", "F"]
print(f"\nSlicing examples with: {full_list}")
print(f"First 3: {full_list[:3]}")  # [A, B, C]
print(f"Last 3: {full_list[-3:]}")  # [D, E, F]
print(f"Middle: {full_list[2:5]}")  # [C, D, E]
print(f"Every 2nd: {full_list[::2]}")  # [A, C, E]
print(f"Reversed: {full_list[::-1]}")  # [F, E, D, C, B, A]

# List methods (many more than C#!)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nNumbers: {numbers}")

# Sorting (like C#'s Sort)
sorted_nums = sorted(numbers)  # Returns new sorted list
print(f"Sorted (new list): {sorted_nums}")
print(f"Original unchanged: {numbers}")

numbers.sort()  # Sort in place (like C#'s Sort)
print(f"Sorted in place: {numbers}")

# Finding elements (like C# IndexOf, Contains)
position = numbers.index(5)  # Find index of first occurrence
print(f"Index of 5: {position}")

count = numbers.count(1)  # Count occurrences
print(f"Count of 1: {count}")

has_element = 9 in numbers  # Check if element exists (like C#'s Contains)
print(f"Contains 9: {has_element}")

# List length (like C#'s Count property)
length = len(numbers)
print(f"Length: {length}")

# Joining lists (like C#'s Concat or AddRange)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # Creates new list
print(f"Combined: {combined}")

list1.extend(list2)  # Add all elements from list2 to list1 (like AddRange)
print(f"Extended list1: {list1}")

# List comprehensions (very Pythonic - no direct C# equivalent until LINQ)
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
print(f"Squares: {squares}")

# Conditional list comprehension
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested lists (like C# jagged arrays)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")
print(f"Element [1][2]: {matrix[1][2]}")  # Access row 1, column 2

# Converting string to list (like C#'s ToCharArray or Split)
text = "Hello"
char_list = list(text)  # Convert string to list of characters
print(f"String to list: {char_list}")

words = "Python is awesome".split()  # Split string into list of words
print(f"Words: {words}")

# Converting list back to string (like C#'s string.Join)
joined = " ".join(words)  # Join with space
print(f"Joined back: {joined}")

# Mixed type lists (impossible in C# without object[])
mixed = ["Alice", 25, True, 3.14, [1, 2, 3]]  # type: ignore
print(f"Mixed types: {mixed}")

# Checking types in mixed list
for i, item in enumerate(mixed): # type: ignore
    print(f"  Index {i}: {item} ({type(item).__name__})") # type: ignore

# List as stack (LIFO - Last In, First Out)
stack = [] 
stack.append("second")  # Push  # type: ignore
stack.append("third")  # Push  # type: ignore
print(f"Stack: {stack}")

last = stack.pop()  # Pop (removes and returns last)  # type: ignore
print(f"Popped: {last}, Remaining: {stack}")


# List copying (important difference from C#!)
original = [1, 2, 3]
reference = original  # This is a reference, not a copy!
shallow_copy = original[:]  # This creates a shallow copy
deep_copy = original.copy()  # This also creates a shallow copy

original.append(4)
print(f"Original: {original}")
print(f"Reference: {reference}")  # Changed because it's the same object!
print(f"Shallow copy: {shallow_copy}")  # Unchanged
print(f"Deep copy: {deep_copy}")  # Unchanged

"""
Key differences from C#:
1. No need to specify type - can hold mixed types
2. Negative indexing (list[-1] for last element)
3. Slicing syntax [start:end:step]
4. List comprehensions for functional-style creation
5. More built-in methods (append, extend, insert, remove, pop, etc.)
6. Reference vs copy behavior
7. Can be used as stack or queue easily
"""
