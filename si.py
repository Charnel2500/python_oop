# Sztuczna inteligencja z różnymi atrybutami

class Robot(object):
    total = 0
    def __init__(self, name, height, weight):
        print("Powstal nowy robot");
        self.name = name
        self.height = height
        self.weight = weight
        Robot.total += 1

    def __str__(self):
        rep = "Obiekt klasy Robot \n"
        rep += "name: " + self.name +"\n" "height: " + str(self.height) +"\n" "weight: " + str(self.weight) +"\n"
        return rep
    def przelicznik(self):
        lbs = 2.2046 * self.weight
        print("Waze ", lbs, " funtow")
    def talk(self):
        print("Czesc! Jestem", self.name, "\n" + "Waze ", self.weight, "kilogramów")

    @staticmethod
    def status():
        print("\nOgolna liczba robotow wynosi ", Robot.total)

#Czesc glowna kodu
sophia = Robot("Sophia",160,55)
sophia.talk()
sophia.przelicznik()

alice = Robot("Alice",150,50)
alice.talk()
print("Wyświetlenie obiektu sophia: \n" + str(sophia) + "\n")
print("Wyświetlenie nazwy obiektu sophia: \n" + sophia.name)
print("Całkowita liczba robotow wynosi " + str(Robot.total))

input("\n Aby zakonczyc program wcisnij enter")
