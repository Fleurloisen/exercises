class Wizard:
    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball = -30
        self.__health += fireball

    def drink_mana_potion(self):
        drink = 40
        self.__mana += drink