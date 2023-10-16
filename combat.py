from character import Character, D6
from creature import Creature
from console import Console

class Combat:
    #COMBAT SYSTEM
    def __init__ (self, player, playerSkill, playerStamina, playerLuck, creature, creatureSkill, creatureStamina):
        self.player = player
        self.playerSkill = playerSkill
        self.playerStamina = playerStamina
        self.playerLuck = playerLuck
        self.creature = creature
        self.creatureSkill = creatureSkill
        self.creatureStamina = creatureStamina
    
    def Wound(self,damage):
        self = self - damage
        return self

    def Heal(self, gain):
        self = self + gain
        return self

    def attackStrengthTest (y, x):
        AttackStrength = D6(2) + x
        print(f"\n{y.upper()} rolled {AttackStrength - x}! | Attack Strength: {AttackStrength}!" )
        return AttackStrength

    def battle(player, playerSkill, playerStamina, playerLuck, creature, creatureSkill, creatureStamina):
        print(f"\nYou encountered {creature.upper()}!")
        while playerStamina and creatureStamina > 0:
            print(f"\n{creature.upper()} | SKILL {creatureSkill} | STAMINA {creatureStamina}")
            print(f"{player.upper()} | {creatureSkill} | STAMINA {playerStamina}")
            print("\n1. ATTACK")
            print("2. ITEM")
            choice = input("Make your choice: ")
            choice = int(choice)
            if choice == 1:
                attack1 = Combat.attackStrengthTest(player, playerSkill)
                attack2 = Combat.attackStrengthTest(creature, creatureSkill)
                if attack1 > attack2:
                    print(f"{creature.upper()} was wounded! (-2 STAMINA)")
                    creatureStamina = Combat.Wound(creatureStamina, 2)
                    print("\n1. Test your luck? (-1 LUCK)")
                    print("2. Continue")
                    choice = input("Make your choice: ")
                    choice = int(choice)
                    if choice == 1:
                        luckTest = Character.luckTest(playerLuck)
                        if luckTest <= playerLuck:
                            print("SUCCESS!")
                            print(f"{creature.upper()} took a serious wound! (-2 STAMINA)")
                            creatureStamina = Combat.Wound(creatureStamina, 2)
                            continue
                        elif luckTest > playerLuck:
                            print("FAIL")
                            print(f"{creature.upper()}'s wound was a mere graze! (+1 STAMINA) ")
                            creatureStamina = Combat.Heal(creatureStamina, 2)
                            continue
                elif attack1 < attack2:
                    print(f"{player.upper()} was wounded! (-2 STAMINA)")
                    playerStamina = Combat.Wound(playerStamina, 2)
                    print("\n1. Test your luck? (-1 LUCK)")
                    print("2. Continue")
                    choice = input("Make your choice: ")
                    choice = int(choice)
                    if choice == 1:
                        luckTest = Character.luckTest(playerLuck)
                        if luckTest <= playerLuck:
                            print("SUCCESS!")
                            print(f"{creature.upper()} took a serious wound! (-2 STAMINA)")
                            creatureStamina = Combat.Wound(creatureStamina, 2)
                            continue
                        elif luckTest > playerLuck:
                            print("FAIL")
                            print(f"{creature.upper()}'s wound was a mere graze! (+1 STAMINA) ")
                            creatureStamina = Combat.Heal(creatureStamina, 2)
                            continue
                else:
                    print("You avoided each others blows!")
                    continue                    
            elif choice == 2:
                print("You are currently holding: ")
                print(f"")
            else:
                print("Try that again...")
        if creatureStamina <= 0:
            print(f"\n{creature.upper()} was defeated!")
        elif playerStamina <= 0:
            print("\nYOU ARE DEAD!")






            


            

                   
