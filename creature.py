def main():
    pass

class Creature:
    def __init__(self, name, skill, stamina):
        self.name = name
        self.skill = skill
        self.stamina = stamina

    def wound(self, damage):
        self.stamina = self.stamina - damage

    def heal(self, stamina):
        self.stamina = self.stamina + stamina