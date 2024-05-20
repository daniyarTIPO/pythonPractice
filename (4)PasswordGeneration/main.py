import random
import string

def generate_password(length=None):
    charecters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(charecters) for _ in range(length))
    return password

def main():
    print("Генератор случайных паролей: ")
    length = int(input("Введите длину пароля: "))
    if length < 8:
        print("Длинна паролья не должна быть меньше 8 символов!")

    else:
        password = generate_password(length)
        print(f"Ваш пароль: {password}")

if __name__ == "__main__":
    main()