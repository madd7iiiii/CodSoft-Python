import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_character = string.punctuation

    characters = lowercase_letters + uppercase_letters + digits + special_character
    

    password = ''.join(random.choice(characters)for _ in range(length))
    return password

def main():
    print("Welcome to the Password generator!")
    
    while True:
        length = int(input("Enter the length of the password (default is 10): \n"))
        if length > 10:
            print("Sorry! You can choose any Number from 1 to 10.")
            break
        password = generate_password(length)
        print(f"Generate Password:{password}")
        
        regenerate = input("Do you want to generate another password? (yes/no): ").lower()

        if regenerate != "yes":
            print("Thanks for using the Password Generator. Goodbye! ")
            break
        
if __name__ == "__main__":
    main()







