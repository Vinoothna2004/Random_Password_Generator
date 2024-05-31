import random
import string

def get_user_input(prompt, validation):
    while True:
        user_input = input(prompt)
        if validation(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_length(input_str):
    return input_str.isdigit() and int(input_str) > 0

def validate_char_types(input_str):
    return set(input_str).issubset(set("lnds"))

def generate_password(length, char_types):
    char_set = ''
    if 'l' in char_types:
        char_set += string.ascii_letters
    if 'n' in char_types:
        char_set += string.digits
    if 's' in char_types:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("No character types selected")

    return ''.join(random.choice(char_set) for _ in range(length))

def main():
    print("Welcome to the Random Password Generator")

    length = int(get_user_input("Enter the desired password length: ", validate_length))
    char_types = get_user_input("Enter character types (l for letters, n for numbers, s for symbols): ", validate_char_types)

    try:
        password = generate_password(length, char_types)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

