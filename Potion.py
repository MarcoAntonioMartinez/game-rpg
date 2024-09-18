class Potion:
    def __init__(self, name, effect, potency):
        self.name = name
        self.effect = effect
        self.potency = potency

    def use(self):
        return f"Using {self.name}, which grants {self.effect} with potency of {self.potency}."


# Health Potions
class HealthPotion(Potion):
    def __init__(self, level):
        if level == "lesser":
            super().__init__("Lesser Health Potion", "heals health", 2)
        elif level == "normal":
            super().__init__("Health Potion", "heals health", 10)
        elif level == "greater":
            super().__init__("Greater Health Potion", "heals health", 20)


# Mana Potions
class ManaPotion(Potion):
    def __init__(self, level):
        if level == "lesser":
            super().__init__("Lesser Mana Potion", "restores mana", 2)
        elif level == "normal":
            super().__init__("Mana Potion", "restores mana", 10)
        elif level == "greater":
            super().__init__("Greater Mana Potion", "restores mana", 20)


# Armor Buff Potions
class ArmorPotion(Potion):
    def __init__(self, level):
        if level == "lesser":
            super().__init__("Lesser Armor Potion", "increases armor", 1)
        elif level == "normal":
            super().__init__("Armor Potion", "increases armor", 4)
        elif level == "greater":
            super().__init__("Greater Armor Potion", "increases armor", 10)


# Magic Buff Potions
class MagicPotion(Potion):
    def __init__(self, level):
        if level == "lesser":
            super().__init__("Lesser Magic Potion", "increases magic", 2)
        elif level == "normal":
            super().__init__("Magic Potion", "increases magic", 10)
        elif level == "greater":
            super().__init__("Greater Magic Potion", "increases magic", 20)


# Berserker Buff Potions
class BerserkerPotion(Potion):
    def __init__(self, level):
        if level == "lesser":
            super().__init__("Lesser Berserker Potion", "increases strength", 2)
        elif level == "normal":
            super().__init__("Berserker Potion", "increases strength", 10)
        elif level == "greater":
            super().__init__("Greater Berserker Potion", "increases strength", 20)
