

def history():
    story = ("Летучие мыши такие классные! Это {}, \n"
           "{} животные, у которых есть крылья. Они любят летать вокруг {},\n"
           "из-за чего некоторые люди их боятся. Но летучие мыши {}, и они не хотят причинять людям вред.\n У "
           "меня есть домашняя летучая мышь, которая живет в \n"
           "{}. Мне нравится кормить его "
           "{} и {}. \nОн Любит "
           "{}. \nЯ его любимый человек, но ему также "
           "нравится {}. \nЯ хочу убедить своих родителей купить "
           "мне {} еще летучих мышей.")

    noun1 = input("Введите цвет: ")
    noun2 = input("Введите прилагательное: ")
    noun3 = input("Введите время: ")
    noun4 = input("Введите прилагательное: ")
    noun5 = input("Введите место: ")
    noun6 = input("Введите еду: ")
    noun7 = input("Введите еду: ")
    noun8 = input("Введите глагол: ")
    noun9 = input("Введите существительное: ")
    noun10 = input("Введите номер: ")

    completed_story = story.format(noun1, noun2, noun3, noun4, noun5, noun6, noun7, noun8, noun9, noun10)
    print("\nВот ваша история: ")
    print(completed_story)

if __name__ == "__main__":
    history()