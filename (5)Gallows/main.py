import random
import os
def choice_world(world_list=None):
    return random.choice(world_list).upper()

def dispaly_curr_prog(word, guessed_letter):
    display = ''.join([letter if letter in guessed_letter else "_" for letter in word])
    return display

def human():
    #module_dir = os.path.dirname(__file__)
    #world_list = os.path.join(module_dir, "sowpods.txt")
    world_list = ["PYTHON","ABORTIFACIENT","ABRADERS", "ABRADES", "ABRAIDING", "ABRANCHIAL", "ABREGE", "ABREGES", "ABRI", "ABRICOCK", "ABRICOCKS", "ABRIDGABLE", "ABRIDGE", "ABRIDGEABLE", "ABRIDGED", "ABRIDGEMENT", "ABRIDGEMENTS", "ABRIDGER", "ABRIDGERS", "ABRIDGES", "ABRIDGING", "ABRIDGMENT", "ABRIDGMENTS", "ABRIM", "ABRIN", "ABRINS", "ABRIS", "ABROACH", "ABROAD", "ABROADS", "ABROGABLE", "ABROGATE", "ABROGATED", "ABROGATES", "ABROGATING", "ABROGATION", "ABROGATIONS", "ABROGATIVE", "ABROGATOR", "ABROGATORS", "ABROOKE", "ABROOKED", "ABROOKES", "ABROOKING", "ABROSIA", "ABROSIAS", "ABRUPT", "ABRUPTER"]
    word = choice_world(world_list)
    guessed_latter = []
    attempts_left = 6
    print("Добро поадловатиь в игру Висильница!")
    print("Угадайте слово по буквам")

    while attempts_left > 0:
        print("\nТекущее слово: " + dispaly_curr_prog(word, guessed_latter))
        print(f"Оставшиеся попытки: {attempts_left}")
        guess = input("Введите букву: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста введите одну букву.")
            continue
        if guess in guessed_latter:
            print("Вы уже угадали эту букву.")
            continue

        guessed_latter.append(guess)

        if guess in word:
            print(f"Отлично! Буква '{guess}' есть в слове")
        else:
            attempts_left -= 1
            print(f"Нет, буквы '{guess}' нетв слове. Попробуйте еще раз.")

        if all(letter in guessed_latter for letter in word):
            print(f"\nПоздравляем! Вы угадали слово: {word}")
            break
    else:
        print(f"\nУ вас закончились попытки. Загаданное слово было: {word}")

if __name__ == "__main__":
    human()