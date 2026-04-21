import random, string, time
print("Welcome to a simple password generator")
print("Auto length is 10 characters")



punct = "*&^%$\£@;:~#]{]}¬`!?</>_" #Set of punctuation that can be generated.
chars = string.ascii_letters + punct # Set of possible characters (letters(a-Z) and punctuation)

def generator_without_length(chars):
    password = "".join(random.choice(chars) for i in range(10))
    return password

def generator_with_length(chars): #Only change is ...in range(length)
    length = int(input("Enter length of random password: "))
    password = "".join(random.choice(chars) for i in range(length))
    return password




while True: # Validation
    user_input = input("\rGenerate with length, yes/no/escape: ").strip().upper()

    if user_input == "YES":
        passwordYL = generator_with_length(chars)
        print(passwordYL)
    elif user_input == "NO":
        passwordNL = generator_without_length(chars)
        print(passwordNL)
    elif user_input == "ESCAPE":
        exit()
    else:
        print("\nInvalid input. Please enter YES or NO.")

            


