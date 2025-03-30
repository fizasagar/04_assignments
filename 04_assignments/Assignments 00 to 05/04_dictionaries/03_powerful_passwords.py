import hashlib

def hash_password(password):
    """Hashes a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the hashed password matches the stored hash for the given email.
    
    Args:
    - email (str): The user's email.
    - password_to_check (str): The password entered by the user.
    - stored_logins (dict): A dictionary with emails as keys and hashed passwords as values.
    
    Returns:
    - bool: True if the password matches, False otherwise.
    """
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

# Example usage:
stored_logins = {
    "user@example.com": hash_password("securepassword123"),
    "admin@example.com": hash_password("adminpass")
}

# Testing login
print(login("user@example.com", "securepassword123", stored_logins))  # True
print(login("admin@example.com", "wrongpassword", stored_logins))  # False
print(login("unknown@example.com", "somepassword", stored_logins))  # False
