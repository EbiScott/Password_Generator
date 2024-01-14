import secrets
import string

choic = int(input("Enter the length of password: "))

def generate_password(length=choic):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Example: Generate a password with default length (12 characters)
password = generate_password()
print("Generated Password:", password)