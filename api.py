import bcrypt

def hash_password(pwd):
    """Hash password"""
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password_bytes, salt)
    return hashed_pwd.decode('utf-8')  

def validate_password(pwd, hashed_pwd):
    password_bytes = pwd.encode('utf-8')
    hashed_pwd_bytes = hashed_pwd.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_pwd_bytes)

def register_user():
    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    hashed_pwd = hash_password(pwd)
    with open("users.txt", "a") as f:
        f.write(f'{username},{hashed_pwd}\n')
        print(f"User {username} registered successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            user, hash = line.strip().split(',', 1)
            if user == username:
                if validate_password(password, hash):
                    print(f"Login successful! Welcome {user}")
                    return True
                else:
                    print("Invalid password.")
                    return False
    print("Username not found.")
    return False