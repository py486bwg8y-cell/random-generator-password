import secrets
import string
from datetime import datetime

PASSWORD_FILE = "password.txt"

def  generate_password(length=16):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password
def save_entry(login, url, password):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    line = f"{timestamp} | {url} | {login} | {password}\n"
    with open(PASSWORD_FILE, "a", encoding="utf=8") as f:
        f.write(line)
    print("Запись сохранена в", PASSWORD_FILE)

def main ():
    print("Генератор паролей")
    
url = input("Введите URL сайта или оставте пустым для выхода").strip()
if url == "":
 print("программа отключена")

login = input("введите логин или электронную почту").strip()

length_input = input("Задайте длину пароля").strip()
if length_input == "":
    length = 16
else:
    try:
       length = int(length_input)
    except ValueError:
        print("некорректное число, использую длину 16")
        length = 16  
password = generate_password(length)
print(f"\nсгенерированный пароль: {password}")
save = input("сохранить запись в файл? (y/n):").strip().lower()
if save == "y":
    save_entry(login, url, password)
else:
    print("запись удалена")
if __name__ == "__main__":
   main()