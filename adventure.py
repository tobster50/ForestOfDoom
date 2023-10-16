from character import Character
from combat import Combat
from creature import Creature
from console import Console

#MAIN MENU
Console.mainMenu(0)

#CHARACTER CREATION AND TUTORIAL
print("\nBefore embarking on your adventure, we need to find out about YOU!")
name = input("What is your name? ")
print(f"\nSo, your name is {name.upper()}! Welcome to FOREST OF DOOM!")
print("In this game your three main stats are SKILL, STAMINA and LUCK")
print("SKILL reflects your swordsmanship and general fighting expertise. The higher the better.")
print("STAMINA reflects your general constitution, your will to survive, your determination and overall fitness.")
print("LUCK - and magic - are facts of life in the fantasy kingdom you are about to explore.")

Console.pause(0)

print("\nNow we must create your character.")
print("Generating...")
skill = Character.skillRoll(0)
stamina = Character.staminaRoll(0)
luck = Character.luckRoll(0)
initial_skill = skill
initial_stamina = stamina
initial_luck = luck
player = Character(name,skill,stamina,luck,initial_skill,initial_stamina,initial_luck)
player.addEquipment('sword')
player.addEquipment('leather armour')
print(player.equipmentList)

print(f"\nYour stats are: SKILL: {player.skill} | STAMINA: {player.stamina} | LUCK: {player.luck}!")
