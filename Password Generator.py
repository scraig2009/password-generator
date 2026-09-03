import random
import string


def get_password_length():
    """Gets and validates the password length."""
    
    while True:
        try:
            password_length = int(input("Enter password length: "))

            if password_length <= 0:
                raise ValueError

            return password_length

        except ValueError:
            print("Error, password length must be an integer greater than 0")


def generate_password(length):
    """Generates a random password."""

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    return password


def main():
    password_length = get_password_length()
    print(f"Your chosen password length is {password_length}")
    password = generate_password(password_length)
    print(f"Generated Password: {password}")


main()