# Exercise 1.1: User Information Processor
# Your task: Complete the missing functions


def process_user_info(
    first_name: str, last_name: str, age: int, email: str = ""
) -> dict:
    """
    Process user information and return a formatted dictionary.

    Args:
        first_name: User's first name
        last_name: User's last name
        age: User's age
        email: User's email (optional)

    Returns:
        Dictionary with processed user information
    """
    # TODO: Complete this function
    # Requirements:
    # 1. Create a full_name by combining first and last name
    # 2. Determine age_category: "Minor" (< 18), "Adult" (18-64), "Senior" (65+)
    # 3. Create a display_name in format "Last, First"
    # 4. Return a dictionary with all the information

    pass  # Remove this and add your code


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

    pass  # Remove this and add your code


def format_user_report(users: list) -> str:
    """
    Create a formatted report of all users.

    Args:
        users: List of user dictionaries

    Returns:
        Formatted string report
    """
    # TODO: Complete this function
    # Requirements:
    # 1. Create a report showing each user's information
    # 2. Format: "Name: [display_name], Age: [age] ([age_category])"
    # 3. If email exists and is valid, add "Email: [email]"
    # 4. Separate each user with a newline

    pass  # Remove this and add your code


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
    processed_users = []
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
