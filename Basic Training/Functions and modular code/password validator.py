def validate_password(**kwargs):
    password = kwargs.get("password", "")

    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    return "Password is strong!"

# Test the function
# print(validate_password(password="Hello123"))  # Output: Password is strong!
# print(validate_password(password="hello123"))  # Output: Password must contain at least one uppercase letter.

