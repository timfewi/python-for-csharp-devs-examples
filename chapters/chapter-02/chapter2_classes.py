# Chapter 2.4: Classes and Objects
# Python vs C# Object-Oriented Programming

"""
C# Class Definition:
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    private string _email;

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public void SayHello()
    {
        Console.WriteLine($"Hello, I'm {Name}");
    }
}
"""


# Python Class Definition - Much simpler syntax!
class Person:
    """A simple Person class demonstrating Python OOP concepts."""

    # Class variable (like C# static field)
    species = "Homo sapiens"

    def __init__(self, name: str, age: int) -> None:
        """Constructor (like C# constructor)."""
        self.name = name  # Public attribute (like C# public property)
        self.age = age
        self._email = ""  # Protected attribute (convention only)
        self.__ssn = ""  # Private attribute (name mangling)

    def say_hello(self) -> None:
        """Instance method (like C# public method)."""
        print(f"Hello, I'm {self.name}")

    def get_info(self) -> str:
        """Return formatted information about the person."""
        return f"{self.name}, {self.age} years old"

    def set_email(self, email: str) -> None:
        """Set email with basic validation."""
        if "@" in email:
            self._email = email
        else:
            print("Invalid email format")

    def get_email(self) -> str:
        """Get email address."""
        return self._email

    # Property using @property decorator (like C# properties)
    @property
    def is_adult(self) -> bool:
        """Check if person is an adult."""
        return self.age >= 18

    @property
    def birth_year(self) -> int:
        """Calculate approximate birth year."""
        from datetime import datetime

        return datetime.now().year - self.age

    # Class method (like C# static method, but with access to class)
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        """Create Person from birth year."""
        from datetime import datetime

        age = datetime.now().year - birth_year
        return cls(name, age)

    # Static method (like C# static method)
    @staticmethod
    def is_valid_age(age: int) -> bool:
        """Check if age is valid."""
        return 0 <= age <= 150

    # String representation (like C# ToString())
    def __str__(self) -> str:
        """String representation for print()."""
        return f"Person(name='{self.name}', age={self.age})"

    def __repr__(self) -> str:
        """Developer representation for debugging."""
        return f"Person('{self.name}', {self.age})"


# Creating objects (same as C#)
person1 = Person("Alice", 25)
person2 = Person("Bob", 17)

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")

# Accessing attributes and methods
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
person1.say_hello()

# Using properties
print(f"Is Alice adult? {person1.is_adult}")
print(f"Is Bob adult? {person2.is_adult}")
print(f"Alice's birth year: {person1.birth_year}")

# Using class methods and static methods
person3 = Person.from_birth_year("Charlie", 1990)
print(f"Person from birth year: {person3}")

print(f"Is age 25 valid? {Person.is_valid_age(25)}")
print(f"Is age -5 valid? {Person.is_valid_age(-5)}")

# Class variables (shared by all instances)
print(f"Species: {Person.species}")
print(f"Alice's species: {person1.species}")
print(f"Bob's species: {person2.species}")

# Modifying class variable affects all instances
Person.species = "Human"
print(f"After change - Alice's species: {person1.species}")


# ===== INHERITANCE =====
class Employee(Person):
    """Employee class inheriting from Person."""

    def __init__(self, name: str, age: int, employee_id: str, salary: float) -> None:
        super().__init__(name, age)  # Call parent constructor
        self.employee_id = employee_id
        self.salary = salary
        self.is_active = True

    def say_hello(self) -> None:
        """Override parent method."""
        print(f"Hello, I'm {self.name}, employee #{self.employee_id}")

    def get_info(self) -> str:
        """Override and extend parent method."""
        base_info = super().get_info()  # Call parent method
        return f"{base_info}, Employee ID: {self.employee_id}"

    def give_raise(self, amount: float) -> None:
        """Method specific to Employee."""
        self.salary += amount
        print(f"{self.name} received a ${amount:,.2f} raise!")

    @property
    def annual_salary(self) -> str:
        """Formatted annual salary."""
        return f"${self.salary:,.2f}"


# Using inheritance
employee = Employee("David", 30, "EMP001", 75000.0)
print(f"\nEmployee: {employee}")
employee.say_hello()  # Calls overridden method
print(f"Employee info: {employee.get_info()}")
print(f"Annual salary: {employee.annual_salary}")

# Employee is also a Person (inheritance)
print(f"Is employee an adult? {employee.is_adult}")  # Uses inherited property
employee.give_raise(5000)
print(f"New salary: {employee.annual_salary}")


# ===== MULTIPLE INHERITANCE =====
class Serializable:
    """Mixin class for serialization functionality."""

    def to_dict(self) -> Dict[str, Any]:
        """Convert object to dictionary."""
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }

    def to_json(self) -> str:
        """Convert object to JSON string."""
        import json

        return json.dumps(self.to_dict(), indent=2)


class Manager(Employee, Serializable):
    """Manager class with multiple inheritance."""

    def __init__(
        self, name: str, age: int, employee_id: str, salary: float, team_size: int
    ) -> None:
        super().__init__(name, age, employee_id, salary)
        self.team_size = team_size
        self.reports: List[Employee] = []

    def add_report(self, employee: Employee) -> None:
        """Add employee to manager's team."""
        self.reports.append(employee)
        print(f"{employee.name} now reports to {self.name}")

    def get_team_info(self) -> str:
        """Get information about manager's team."""
        if not self.reports:
            return f"{self.name} manages a team of {self.team_size} (no direct reports tracked)"

        report_names = [emp.name for emp in self.reports]
        return f"{self.name} manages: {', '.join(report_names)}"


# Using multiple inheritance
manager = Manager("Eva", 35, "MGR001", 95000.0, 5)
manager.add_report(employee)

print(f"\nManager: {manager}")
print(f"Team info: {manager.get_team_info()}")

# Using serialization from mixin
print(f"\nManager as JSON:")
print(manager.to_json())


# ===== SPECIAL METHODS (MAGIC METHODS) =====
class Point:
    """Point class demonstrating special methods."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """String representation."""
        return f"Point({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Developer representation."""
        return f"Point({self.x!r}, {self.y!r})"

    def __eq__(self, other: object) -> bool:
        """Equality comparison."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":
        """Addition operator."""
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self) -> int:
        """Length (distance from origin)."""
        return int((self.x**2 + self.y**2) ** 0.5)


# Using special methods
p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"\nPoints:")
print(f"p1: {p1}")
print(f"p2: {p2}")

print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")

p4 = p1 + p2  # Uses __add__
print(f"p1 + p2 = {p4}")

print(f"Length of p1: {len(p1)}")  # Uses __len__

# ===== DATACLASSES (Modern Python) =====
from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class Product:
    """Product class using dataclass decorator."""

    name: str
    price: float
    category: str = "General"
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Called after initialization."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")

    @property
    def formatted_price(self) -> str:
        """Format price as currency."""
        return f"${self.price:.2f}"


# Using dataclass
product = Product("Laptop", 999.99, "Electronics", ["computer", "portable"])
print(f"\nProduct: {product}")
print(f"Formatted price: {product.formatted_price}")

# Dataclass automatically generates __init__, __repr__, __eq__, etc.
product2 = Product("Laptop", 999.99, "Electronics", ["computer", "portable"])
print(f"Products equal: {product == product2}")

"""
Key differences from C#:
1. No access modifiers (public/private) - use naming conventions
2. self parameter required for instance methods
3. @property decorator for properties
4. Multiple inheritance supported
5. Special methods (__str__, __eq__, etc.) for operator overloading
6. @dataclass decorator for automatic method generation
7. Duck typing - no interface declarations needed
8. @classmethod and @staticmethod decorators
9. Mixin classes for shared functionality
10. No need for explicit interface implementations
"""
