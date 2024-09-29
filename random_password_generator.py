import random
import string


def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    """Generate a random password based on the specified criteria."""

    # Define character sets based on user preferences
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    print("Password Generator")

    # Get user input
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
            return

        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        # Generate and display the password
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
