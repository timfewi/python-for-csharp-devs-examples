# Chapter 1.4: Functions
# Python vs C# Function/Method Declaration

"""
C# Method Declaration:
public static int CalculateSum(int a, int b) {
    return a + b;
}

public static string GreetUser(string name, string greeting = "Hello") {
    return $"{greeting}, {name}!";
}
"""

# Python Function Declaration - Much simpler!


def calculate_int_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers."""  # Docstring (like C# XML comments)
    return a + b

def calculate_float_sum(a: float, b: float) -> float:
    """Calculate the sum of two floating-point numbers."""
    return a + b

def greet_user(name: str, greeting: str = "Hello") -> str:
    """Greet a user with a customizable greeting."""
    return f"{greeting}, {name}!"


# Basic function calls
result = calculate_int_sum(5, 3)
print(f"Sum: {result}")

message = greet_user("Alice")
print(f"Default greeting: {message}")

message = greet_user("Bob", "Hi")
print(f"Custom greeting: {message}")

# Python's keyword arguments (very powerful!)
message = greet_user(greeting="Hey", name="Charlie")  # Order doesn't matter!
print(f"Keyword args: {message}")


# Functions with multiple return values (unlike C#!)
def get_name_parts(full_name: str) -> tuple[str, str]:
    """Split a full name into first and last name."""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]  # Returns a tuple!
    return parts[0], ""


first, last = get_name_parts("John Doe")  # Tuple unpacking!
print(f"First: {first}, Last: {last}")


# Variable arguments (*args and **kwargs - very Python-specific!)
def print_info(*args, **kwargs):
    """Print all arguments and keyword arguments."""
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")


print_info("Alice", 25, city="New York", active=True)


# Type hints (optional, like C# but added later)
def add_numbers(a: int, b: int) -> int:
    """Add two integers with type hints."""
    return a + b


def format_name(first: str, last: str) -> str:
    """Format a full name with type hints."""
    return f"{first} {last}".title()


# Type hints help IDEs and tools, but don't enforce types at runtime
typed_sum = add_numbers(10, 20)
print(f"Typed sum: {typed_sum}")

formatted = format_name("john", "doe")
print(f"Formatted name: {formatted}")

# Python functions are first-class objects (unlike C# methods)
my_function = calculate_sum  # Assign function to variable
result = my_function(7, 8)
print(f"Function as variable: {result}")

# Lambda functions (Python's version of C# lambda expressions)
square = lambda x: x * x
numbers = [1, 2, 3, 4, 5]
squared = [square(n) for n in numbers]  # List comprehension!
print(f"Squared numbers: {squared}")
