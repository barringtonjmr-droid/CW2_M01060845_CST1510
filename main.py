from api import register_user, login

def menu():
    print("\nPlease choose an option:")
    print("1 - Register User")
    print("2 - Login")
    print("3 - Exit")

def main():
    """Runs program"""
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Closing program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
