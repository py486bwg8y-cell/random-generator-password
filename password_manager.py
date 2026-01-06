import secrets
import string
from datetime import datetime

PASSWORD_FILE = "password.txt"

def  generate_password(length=16):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password