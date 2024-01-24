import pytest
from password_generator import generate_password

def test_generate_password_length():
    length = 10
    password = generate_password(length)
    assert len(password) == length

def test_generate_password_characters():
    length = 10
    password = generate_password(length)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+={[}]|:;<,>.?/~"
    assert all(char in characters for char in password)
