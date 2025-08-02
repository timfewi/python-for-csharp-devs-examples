# Chapter 1.2: String Operations
# Python vs C# String Handling

"""
C# String Operations:
string firstName = "John";
string lastName = "Doe";
string fullName = firstName + " " + lastName;
string formatted = $"Hello, {fullName}!";
string upper = fullName.ToUpper();
"""

# Python String Operations
first_name = "John"
last_name = "Doe"

# Concatenation (similar to C#)
full_name = first_name + " " + last_name
print(f"Concatenation: {full_name}")

# F-strings (Python's version of C# string interpolation)
formatted = f"Hello, {full_name}!"
print(f"F-string: {formatted}")

# String methods (similar to C# but lowercase with underscores)
upper_name = full_name.upper()  # C#: ToUpper()
lower_name = full_name.lower()  # C#: ToLower()
title_name = full_name.title()  # Similar to C#'s ToTitleCase()

print(f"Upper: {upper_name}")
print(f"Lower: {lower_name}")
print(f"Title: {title_name}")

# String methods that don't exist in C# (or are different)
words = full_name.split()  # Splits by whitespace
print(f"Split words: {words}")

joined = "-".join(words)  # Joins with separator
print(f"Joined with dash: {joined}")

# Multi-line strings (different from C#)
multi_line = """This is a
multi-line string
in Python"""
print(f"Multi-line:\n{multi_line}")

# String slicing (very different from C#!)
text = "Hello, World!"
print(f"First 5 chars: {text[:5]}")  # "Hello"
print(f"Last 6 chars: {text[-6:]}")  # "World!"
print(f"Middle chars: {text[7:12]}")  # "World"
