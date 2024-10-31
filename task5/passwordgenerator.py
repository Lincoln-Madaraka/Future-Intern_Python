import random
import string

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def generate_password():
    print("Welcome to the Password Generator!")
    
    # Ask for user criteria
    try:
        length = int(input("Enter the password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Criteria options with validation
    use_uppercase = get_yes_no_input("Include uppercase letters? (y/n): ")
    use_lowercase = get_yes_no_input("Include lowercase letters? (y/n): ")
    use_digits = get_yes_no_input("Include numbers? (y/n): ")
    use_symbols = get_yes_no_input("Include symbols? (y/n): ")

    # Build the character pool and enforce at least one of each selected type
    character_pool = []
    guaranteed_chars = []

    if use_uppercase:
        character_pool.extend(string.ascii_uppercase)
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        character_pool.extend(string.ascii_lowercase)
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        character_pool.extend(string.digits)
        guaranteed_chars.append(random.choice(string.digits))
    if use_symbols:
        character_pool.extend(string.punctuation)
        guaranteed_chars.append(random.choice(string.punctuation))

    # Ensure character pool is not empty
    if not character_pool:
        print("You need to select at least one character type to generate a password.")
        return

    # Adjust length to ensure guaranteed characters are included
    remaining_length = length - len(guaranteed_chars)
    if remaining_length < 0:
        print("Password length is too short for selected criteria.")
        return

    # Generate the remaining part of the password
    random_part = [random.choice(character_pool) for _ in range(remaining_length)]
    password_list = guaranteed_chars + random_part
    random.shuffle(password_list)

    # Convert list to string
    password = ''.join(password_list)
    print(f"Generated Password: {password}")

generate_password()

