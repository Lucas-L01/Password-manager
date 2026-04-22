import os
from storage import load_data, save_data
from crypto_utils import setup, login

def add_password():
    service = input("Service: ")
    username = input("Username: ")
    password = input("Password: ")

    data = load_data()

    data.append({
        "service": service,
        "username": username,
        "password": password
    })

    save_data(data)
    print("Saved!")

def show_passwords():
    data = load_data()

    for entry in data:
        print(entry["service"], entry["username"], entry["password"])

def main():
    if not os.path.isdir("data"):
        setup()
    else:
        login()
    while True:
        print("\n1. Add password")
        print("2. Show passwords")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            add_password()
        elif choice == "2":
            show_passwords()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()