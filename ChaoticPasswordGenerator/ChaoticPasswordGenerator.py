import random
import string
import re
def method_name():
    import pyperclip
    return pyperclip

pyperclip = method_name()


def is_valid_password(password: str) -> bool:
    """
    Checks if the given password meets the desired requirements.
    :param password: The password to check.
    :return: True if the password is valid, False otherwise.
    """
    # specify desired requirements
    has_upper = re.search("[A-Z]", password) is not None
    has_lower = re.search("[a-z]", password) is not None
    has_digit = re.search("[0-9]", password) is not None
    has_special = re.search("[!@#$%^&*(),.?\":{}|<>]", password) is not None

    return has_upper and has_lower and has_digit and has_special

def generate_password(length: int = 12) -> str:
    """
    Generates a random password of the specified length.
    :param length: The desired length of the password.
    :return: A randomly generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if is_valid_password(password):
            return password

while True:
    try:
        password_length = int(input("Enter the desired length of the password (or 0 to exit): "))
        if password_length == 0:
            break
        elif password_length > 0:
            password = generate_password(password_length)
            if is_valid_password(password):
                print(password)
                pyperclip.copy(password)
                print("The password has been copied to the clipboard.")
            else:
                print("The generated password does not meet the desired requirements.")
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if is_valid_password(password):
    print(password)
    pyperclip.copy(password)
    print("The password has been copied to the clipboard.")
else:
    print("The generated password does not meet the desired requirements.")
