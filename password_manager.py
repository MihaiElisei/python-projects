from cryptography.fernet import Fernet
import os

# Function to generate and store a new encryption key
# This should only be run once to generate a persistent key

def write_key():
    if not os.path.exists("key.key"):  # Prevent overwriting the key
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

# Function to load the encryption key from a file
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Ensure a key exists
write_key()
key = load_key()
fer = Fernet(key)  # Correctly initialize Fernet with the key

# Function to view stored passwords
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                user, encrypted_pass = line.strip().split(" | ")
                decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                print(f"User: {user}, Password: {decrypted_pass}")
    except FileNotFoundError:
        print("No passwords stored yet.")
    except Exception as e:
        print(f"Error reading passwords: {e}")

# Function to add new passwords
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + encrypted_pwd + "\n")
    print("Password added successfully!")

# Main program loop
while True:
    mode = input("Would you like to add a new password or view existing ones? [view/add]. Press 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode, please choose 'view' or 'add'.")
