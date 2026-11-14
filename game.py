import random

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self._hp = hp         
        self._power = power

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def take_damage(self, damage):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0

    def attack(self, target):
        damage = self._power
        target.take_damage(damage)
        print(f"{self.name} атакует {target.name}! Урон: {damage}. У {target.name} осталось {target.get_hp()} HP.")


class Elf(Character):
    def attack(self, target):
        damage = self._power + random.randint(5, 15) # Эльфы бьют магией (случайный урон)
        target.take_damage(damage)
        print(f"🧝‍♂️ Эльф {self.name} стреляет магией в {target.name}! Урон: {damage}. У {target.name} осталось {target.get_hp()} HP.")

class Orc(Character):
    def attack(self, target):
        damage = self._power + 10 # Орки бьют очень сильно
        target.take_damage(damage)
        print(f"👹 Орк {self.name} бьет дубиной {target.name}! Урон: {damage}. У {target.name} осталось {target.get_hp()} HP.")

class Dwarf(Character):
    def attack(self, target):
        damage = self._power + random.randint(0, 5)
        target.take_damage(damage)
        print(f"🧔 Гном {self.name} рубит топором {target.name}! Урон: {damage}. У {target.name} осталось {target.get_hp()} HP.")

class Human(Character):
    def attack(self, target):
        damage = self._power
        target.take_damage(damage)
        print(f"🧑 Человек {self.name} атакует мечом {target.name}! Урон: {damage}. У {target.name} осталось {target.get_hp()} HP.")



class HeroFactory:
    @staticmethod
    def create_hero(hero_type, name):
        
        if hero_type == "elf":
            return Elf(name, hp=80, power=15)
        elif hero_type == "orc":
            return Orc(name, hp=120, power=20)
        elif hero_type == "dwarf":
            return Dwarf(name, hp=100, power=18)
        elif hero_type == "human":
            return Human(name, hp=90, power=16)
        else:
            raise ValueError("Неизвестный тип героя!")



def main():
    print("=== СОЗДАНИЕ ГЕРОЕВ ЧЕРЕЗ ФАБРИКУ ===")
    
        HeroFactory.create_hero("elf", "Леголас"),
        HeroFactory.create_hero("orc", "Азог"),
        HeroFactory.create_hero("dwarf", "Гимли"),
        HeroFactory.create_hero("human", "Арагорн")
    ]

    print("На арену выходят: " + ", ".join([h.name for h in heroes]))
    
    round_num = 1
    
    while len([h for h in heroes if h.is_alive()]) > 1:
        print(f"\n--- РАУНД {round_num} ---")
        
        
        alive_heroes = [h for h in heroes if h.is_alive()]
        
      
        attacker = random.choice(alive_heroes)
        possible_targets = [h for h in alive_heroes if h != attacker]
        target = random.choice(possible_targets)

        
        attacker.attack(target)

        if not target.is_alive():
            print(f"💀 {target.name} ПОВЕРЖЕН!")

        round_num += 1

   
    winner = [h for h in heroes if h.is_alive()][0]
    print(f"\n🏆 ПОБЕДИТЕЛЬ: {winner.name}!")

if __name__ == "__main__":
    main()
    
