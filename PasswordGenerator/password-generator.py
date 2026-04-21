import random, string, time
print("Auto length is 10 characters")



punct = "*&^%$\£@;:~#]{]}¬`!?</>_" #Set of punctuation that can be generated.
chars = string.ascii_letters + punct # Set of possible characters (letters(a-Z) and punctuation)

def generator_without_length(chars):
    password = "".join(random.choice(chars) for i in range(10))
    return password




while True: # Validation
    user_input = input("\rGenerate with length, yes or no: ").strip().upper()

    if user_input == "YES":
        length_choice = True
        break
    elif user_input == "NO":
        length_choice = False
        break
    else:
        print("Invalid input. Please enter YES or NO.")


if length_choice:
    passwordWL = generator_without_length(chars)
    print(passwordWL)