import random, time

print('''Witaj w grze, w której toczysz walke na smierc i zycie z roznymi przerazajacymi przeciwnikami.
Do wyboru masz trzy frakcje: Pozaswiat, Czelusc i Ziemie. Wybierz najpierw frakcje. Potem wybierz
wojownika z danej frakcji, a potem walcz z losowym przeciwnikiem\n\n\n''')

time.sleep(2)
username = input("What is your name?\n")
print("Hi " + username + "!")

faction = input("Choose your faction. Give me a number. 1. Outworld, 2. Netherrealm, 3. Earth\n")

while faction != "1" and faction != "2" and faction != "3":
    print("Wrong. Write just number: 1 or 2 or 3!")
    faction = input("Choose your faction. Give me a number. 1. Outworld, 2. Netherrealm, 3. Earth\n")


print("You choose" + faction)

class Fighter(object):

    total = 0
    def __init__(self, name, attack, hp, defense, regeneration):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.defense = defense
        self.regeneration = regeneration
        Fighter.total += 1

class Outworld_Fighter(Fighter):
    def __str__(self):
        rep = "Jestem wojownikiem z Outworld \n"
        return rep


class Netherrealm_Fighter(Fighter):
    def __str__(self):
        rep = "Jestem wojownikiem z Outworld \n"
        return rep
class Earth(Fighter):
    def __str__(self):
        rep = "Jestem wojownikiem z Outworld \n"
        return rep

kitana = Outworld_Fighter("Kitana",100, 1200, 80, 50)
print("Wyświetlenie obiektu Kitana: \n" + str(kitana) + "\n")
