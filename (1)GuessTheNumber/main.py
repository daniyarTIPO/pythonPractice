import random


def guessTheNumber():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Компьютер загадал число от 1 до 10. Попробуй угадай его")
    while guess != secret_number:
        guess = int(input("Введите ваше число: "))
        attempts += 1
        if(guess < secret_number):
            print("Загаданное число больше")
        elif(guess > secret_number):
            print("Загаданное число меньше")
        else:
            print(f"Поздравляю! Вы отгадали число {secret_number} за попыток {attempts}")


if __name__ == '__main__':
    guessTheNumber()

