# Sztuczna inteligencja z różnymi atrybutami

class Robot(object):
    total = 0
    def __init__(self, name, height, weight, mood):
        print("Powstal nowy robot");
        self.name = name
        self.height = height
        self.weight = weight
        self.__mood = mood
        Robot.total += 1


    def __str__(self):
        rep = "Obiekt klasy Robot \n"
        rep += "name: " + self.name +"\n" "height: " + str(self.height) +"\n" "weight: " + str(self.weight) +"\n"
        return rep
    def przelicznik(self):
        lbs = 2.2046 * self.weight
        return lbs
    def talk(self):
        print("Czesc! Jestem", self.name, "\n" + "Waze ", self.weight, "kilogramów, czyli tyle funtów", self.przelicznik())
        print("Mój nastrój określam jako: ", self.__mood,"\n")
        self.__sekret()


    @staticmethod
    def status():
        print("\nOgolna liczba robotow wynosi ", Robot.total)

    def __sekret(self):
        print("Sekretem każdego robota jest to, ze nie ma zadnego sekretu.")
#Czesc glowna kodu
sophia = Robot("Sophia",160,55, "smutny")
sophia.talk()
sophia.przelicznik()

alice = Robot("Alice",150,50, "zadowolony")
alice.talk()
print("Wyświetlenie obiektu sophia: \n" + str(sophia) + "\n")
print("Wyświetlenie nazwy obiektu sophia: \n" + sophia.name)
print("Całkowita liczba robotow wynosi " + str(Robot.total))

input("\n Aby zakonczyc program wcisnij enter")
