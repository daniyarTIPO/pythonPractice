import random

def roll_dice():
    return random.randint(1, 6)

def dice_game():
    print("Кости!")
    play_again = True

    while play_again:
        input("Нажмите ENTER,чтобы бросить кости...")
        dice1 = roll_dice()
        dice2 = roll_dice()
        print(f"Вы бросили кости и выпало: {dice1} and {dice2}")
        print(f"Общая сумма: {dice1 + dice2}")

if __name__ == "__main__":
    dice_game()
