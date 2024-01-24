import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+={[}]|:;<,>.?/~"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

length = 10
password = generate_password(length)
print(password)
