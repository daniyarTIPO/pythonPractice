import random

def to_play_SCP():
    option = ["камень", "ножницы", "бумага"]
    playAgain = True

    print("Давай сыграем в 'Камень, ножницы, бумага!'")
    while playAgain:
        computer_choice = random.choice(option)
        playerChoice = input("Выберите: Камень, ножницы или бумага: ").lower()

        if playerChoice not in option:
            print("Неправильный выбор")
            continue
        print(f"Компьютер выбрал {computer_choice}")

        if playerChoice == computer_choice:
            print("")
        elif (playerChoice == "камень" and computer_choice == "ножницы") or (playerChoice == "ножнцы" and computer_choice == "бумага") or (playerChoice == "бумага" and computer_choice == "камень"):
            print("Вы выиграли")
        else:
            print("Вы проиграли")

        play_again_input = input("Хотите поиграть еще раз? (д/н): ").lower()
        if play_again_input != 'д':
            print("Спасибо за игру!")
            playAgain = False
        else:
            print("Новая игра!")


if __name__ == '__main__':
    to_play_SCP()