import random
def random_():
    rand = random.randint(1, 100)
    i = 0
    while i < 5:
        word = int(input("Введите число: "))
        if word == rand:
            print("Равно")
            break
        elif word < rand:
            print("Меньшее")
        else: 
            print("Больше")
        i += 1
    else:
        print("Вы не угадали")
random_()