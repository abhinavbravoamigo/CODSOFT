import random
import string

def main():
    print("Password Generator")
    length = password_length()
    complexity = password_complexity()
    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")
    exit=input("Press Enter to exit")

def password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def password_complexity():
    complexity = input("Include special characters? (yes/no): ").lower()
    if complexity=="yes":
        complexity=True
    elif complexity=="no":
        complexity=False
    return complexity

def generate_password(length, complexity):
    if complexity:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    main()