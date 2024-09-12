#character_classes.py

class Character:
    def __init__(self, job_name, hp, defense, evasion, strength, speed, mana):
        self.job_name = job_name
        self.stats = {
            'hp': hp,
            'defense': defense,
            'evasion': evasion,
            'strength': strength,
            'speed': speed,
            'mana': mana
        }
        self.level = 1
        self.points_allocated_this_level = 0

    def increase_stat(self, amount):
        if self.points_allocated_this_level + amount > 3:
            print(f"Cannot increase by {amount} points. You can only increase by {3 - self.points_allocated_this_level} more points this level.")
            return

        print("Which stat would you like to increase?")
        for stat in self.stats:
            print(f"- {stat.capitalize()}: {self.stats[stat]}")

        stat_choice = input("Enter the stat you want to increase: ").lower()

        if stat_choice in self.stats:
            self.stats[stat_choice] += amount
            self.points_allocated_this_level += amount
            print(f"{stat_choice.capitalize()} increased by {amount}!")
        else:
            print("Invalid stat choice!")

    def level_up(self):
        self.level += 1
        self.points_allocated_this_level = 0
        print(f"Level up! You are now at level {self.level}.")

    def display_stats(self):
        return {
            "Job": self.job_name,
            "Level": self.level,
            "Stats": self.stats
        }

class Necromancer(Character):
    def __init__(self):
        super().__init__(job_name="Necromancer", hp=4, defense=5, evasion=4, strength=4, speed=5, mana=8)

class Bard(Character):
    def __init__(self):
        super().__init__(job_name="Bard", hp=6, defense=4, evasion=6, strength=3, speed=5, mana=6)

class Warrior(Character):
    def __init__(self):
        super().__init__(job_name="Warrior", hp=7, defense=6, evasion=3, strength=7, speed=4, mana=3)

class Thief(Character):
    def __init__(self):
        super().__init__(job_name="Thief", hp=5, defense=4, evasion=7, strength=6, speed=5, mana=3)

class Mage(Character):
    def __init__(self):
        super().__init__(job_name="Mage", hp=5, defense=4, evasion=4, strength=3, speed=6, mana=8)

class Paladin(Character):
    def __init__(self):
        super().__init__(job_name="Paladin", hp=6, defense=5, evasion=3, strength=5, speed=4, mana=7)

class Archer(Character):
    def __init__(self):
        super().__init__(job_name="Archer", hp=6, defense=3, evasion=3, strength=6, speed=6, mana=6)

class Priest(Character):
    def __init__(self):
        super().__init__(job_name="Priest", hp=6, defense=6, evasion=6, strength=1, speed=5, mana=6)

class MartialArtist(Character):
    def __init__(self):
        super().__init__(job_name="Martial Artist", hp=6, defense=7, evasion=5, strength=8, speed=4, mana=3)
