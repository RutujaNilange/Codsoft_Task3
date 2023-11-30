import random
import string

def gen_pass(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(len))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            len = int(input("Length of the Password to be(in numbers): "))
            if len <= 0:
                raise ValueError("Enter a positive number.")
            break
        except ValueError:
            print("Error.Enter a valid number.")

    password = gen_pass(len)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
