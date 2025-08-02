# Exercise 1.1: User Information Processor
# Your task: Complete the missing functions

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class AgeCategory(Enum):
    """Enumeration for age categories."""

    MINOR = "Minor"
    ADULT = "Adult"
    SENIOR = "Senior"


@dataclass
class User:
    """User data class with type safety."""

    first_name: str
    last_name: str
    age: int
    email: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate user data after initialization."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if not self.first_name.strip():
            raise ValueError("First name cannot be empty")
        if not self.last_name.strip():
            raise ValueError("Last name cannot be empty")

    @property
    def full_name(self) -> str:
        """Get the full name combining first and last name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def display_name(self) -> str:
        """Get the display name in 'Last, First' format."""
        return f"{self.last_name}, {self.first_name}"

    @property
    def age_category(self) -> AgeCategory:
        """Determine age category based on age."""
        if self.age < 18:
            return AgeCategory.MINOR
        elif self.age <= 64:
            return AgeCategory.ADULT
        else:
            return AgeCategory.SENIOR

    @property
    def is_email_valid(self) -> bool:
        """Check if the user's email is valid."""
        return validate_email(self.email or "")

    def to_dict(self) -> dict[str, str | int | None]:
        """Convert User object to dictionary for backward compatibility."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "full_name": self.full_name,
            "display_name": self.display_name,
            "age_category": self.age_category.value,
            "is_email_valid": self.is_email_valid,
        }


def process_user_info(
    first_name: str, last_name: str, age: int, email: str = ""
) -> User:
    """
    Process user information and return a User object.

    Args:
        first_name: User's first name
        last_name: User's last name
        age: User's age
        email: User's email (optional)

    Returns:
        User object with processed information
    """
    # TODO: Complete this function
    # Requirements:
    # 1. Create a User object with the provided information
    # 2. The User class handles full_name, display_name, and age_category automatically
    # 3. Pass email as None if empty string is provided

    email_value = email if email else None
    return User(first_name, last_name, age, email_value)


def validate_email(email: str) -> bool:
    """
    Simple email validation - check if email contains @ and .

    Args:
        email: Email string to validate

    Returns:
        True if email appears valid, False otherwise
    """
    # TODO: Complete this function
    # Requirements:
    # 1. Check if email contains both "@" and "."
    # 2. Check if email is not empty
    # 3. Return True if valid, False otherwise

    if email and "@" in email and "." in email:
        return True
    return False


def format_user_report(users: List[User]) -> str:
    """
    Create a formatted report of all users.

    Args:
        users: List of User objects

    Returns:
        Formatted string report
    """
    # TODO: Complete this function
    # Requirements:
    # 1. Create a report showing each user's information
    # 2. Format: "Name: [display_name], Age: [age] ([age_category])"
    # 3. If email exists and is valid, add "Email: [email]"
    # 4. Separate each user with a newline

    report_lines: List[str] = []
    for user in users:
        line = f"Name: {user.display_name}, Age: {user.age} ({user.age_category.value})"
        if user.email and user.is_email_valid:
            line += f", Email: {user.email}"
        report_lines.append(line)

    return "\n".join(report_lines)


# Test your functions
if __name__ == "__main__":
    # Test data
    test_users = [
        ("John", "Doe", 25, "john.doe@email.com"),
        ("Jane", "Smith", 17, "jane@example.com"),
        ("Bob", "Johnson", 70, ""),
        ("Alice", "Brown", 30, "invalid-email"),
    ]

    # Process each user
    processed_users: List[User] = []
    for first, last, age, email in test_users:
        user_info = process_user_info(first, last, age, email)
        processed_users.append(user_info)

    # Generate and print report
    report = format_user_report(processed_users)
    print("User Report:")
    print(report)

    # Test email validation separately
    print("\nEmail Validation Tests:")
    test_emails = ["test@example.com", "invalid-email", "", "user@domain.org"]
    for email in test_emails:
        is_valid = validate_email(email)
        print(f"'{email}' is {'valid' if is_valid else 'invalid'}")

    # Test User validation
    print("\nUser Validation Tests:")
    try:
        invalid_user = User("", "Smith", 25)  # Empty first name
        print("Empty first name validation failed!")
    except ValueError as e:
        print(f"✓ Caught invalid first name: {e}")

    try:
        invalid_user = User("John", "", 25)  # Empty last name
        print("Empty last name validation failed!")
    except ValueError as e:
        print(f"✓ Caught invalid last name: {e}")

    try:
        invalid_user = User("John", "Doe", -5)  # Negative age
        print("Negative age validation failed!")
    except ValueError as e:
        print(f"✓ Caught invalid age: {e}")

    # Test to_dict method
    print("\nUser to_dict() example:")
    sample_user = User("Alice", "Johnson", 28, "alice@example.com")
    user_dict = sample_user.to_dict()
    print(f"User as dict: {user_dict}")

# Expected output:
"""
User Report:
Name: Doe, John, Age: 25 (Adult), Email: john.doe@email.com
Name: Smith, Jane, Age: 17 (Minor), Email: jane@example.com
Name: Johnson, Bob, Age: 70 (Senior)
Name: Brown, Alice, Age: 30 (Adult)

Email Validation Tests:
'test@example.com' is valid
'invalid-email' is invalid
'' is invalid
'user@domain.org' is valid
"""
