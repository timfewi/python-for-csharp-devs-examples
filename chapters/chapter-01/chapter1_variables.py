# Chapter 1.1: Variables and Basic Data Types
# Python vs C# Comparison

"""
C# Variable Declaration:
string name = "John";
int age = 30;
double salary = 75000.50;
bool isActive = true;
"""

# Python Variable Declaration - No type declaration needed!
name = "John"  # string (called 'str' in Python)
age = 30  # integer (called 'int' in Python)
salary = 75000.50  # float (Python's equivalent to double)
is_active = True  # boolean (called 'bool' in Python)

# Python can dynamically change types (C# cannot without casting)
my_variable = "Hello"  # string
print(f"my_variable is a {type(my_variable).__name__}: {my_variable}")

my_variable = 42  # now it's an integer!
print(f"my_variable is now a {type(my_variable).__name__}: {my_variable}")

# Type checking in Python
print(f"name type: {type(name)}")
print(f"age type: {type(age)}")
print(f"salary type: {type(salary)}")
print(f"is_active type: {type(is_active)}")

# Python naming convention: snake_case (vs C#'s PascalCase/camelCase)
user_name = "john_doe"  # Python style
total_amount = 1000.0  # Python style
is_logged_in = False  # Python style
