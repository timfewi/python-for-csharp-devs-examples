# Chapter 1.3: Control Flow
# Python vs C# Control Structures

"""
C# Control Flow:
if (condition) {
    // code
} else if (anotherCondition) {
    // code
} else {
    // code
}

for (int i = 0; i < 10; i++) {
    // code
}

while (condition) {
    // code
}
"""

# Python Control Flow - Notice: NO BRACES! Indentation matters!

# If-elif-else (Python's version of if-else if-else)
age = 25
status = ""

if age < 18:
    status = "Minor"
elif age < 65:
    status = "Adult"
else:
    status = "Senior"

print(f"Age {age} = {status}")

# For loops - Very different from C#!
print("\nFor loop examples:")

# Range-based for loop (similar to C#'s for loop)
print("Numbers 0-4:")
for i in range(5):  # range(5) gives 0,1,2,3,4
    print(f"  {i}")

print("Numbers 1-5:")
for i in range(1, 6):  # range(1, 6) gives 1,2,3,4,5
    print(f"  {i}")

print("Even numbers 0-10:")
for i in range(0, 11, 2):  # range(start, stop, step)
    print(f"  {i}")

# Iterating over collections (very Pythonic!)
names = ["Alice", "Bob", "Charlie"]
print("\nIterating over names:")
for name in names:  # No indexing needed!
    print(f"  Hello, {name}!")

# While loops (similar to C#)
count = 0
print(f"\nWhile loop countdown:")
while count < 3:
    print(f"  Count: {count}")
    count += 1  # Note: No ++ operator in Python!

# Python's truthiness concept (different from C#)
print(f"\nPython truthiness:")
values: list[bool | int | str | list | None] = [True, False, 0, 1, "", "hello", [], [1, 2, 3], None] # type: ignore

for value in values: # type: ignore
    if value:  # Python evaluates truthiness
        print(f"  {value} is truthy")
    else:
        print(f"  {value} is falsy")
