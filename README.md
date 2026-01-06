Разбор кода:
1.
import secrets - подключаем модуль который умеет подбтрать безопасные значения символов.
impport string - подключаем модуль где лежат готовые наборы символов. (для автоматизации процесса)
from datetime import datetime - метка с датой и временем для каждого пароля.

2.
PASSWORD_FILE = "password.txt":

PASSWORD_FILE - переменная.
"password.txt" - файл с списком паролей и времени его создания.

3.
def  generate_password(length=16) - функция которая по умолчанию имеет параметр 16 символов.

4.
characters = string.ascii_letters + string.digits + string.punctuation - список символов для создания пароля.

characters = буквы + цифры + спецсимволы

5.
password = "".join(secrets.choice(characters) for _ in range(length)) - сама генерация пароля и сохранение в переменную password

6.
return password - завершить процесс и выдать значение пароля
