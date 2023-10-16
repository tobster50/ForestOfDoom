import random

#FOR ANY DICE ROLLS USE D6 FUNCTION. (D) = HOW MANY D6 YOU WISH TO ROLL
def D6 (d):
        if d == 1:
            return random.randint(1,6)
        else:
            return random.randint(1,6) * d
    
class Character:
    #CHARACTER CREATION. DEFINE INITIAL SKILL STAMINA AND LUCK
    def __init__(self, name, skill, stamina, luck, initial_skill, initial_stamina, initial_luck):
         self.name = name
         self.skill = skill
         self.stamina = stamina
         self.luck = luck 
         self.initial_skill = initial_skill
         self.initial_stamina = initial_stamina
         self.initial_luck = initial_luck
         self.gold = 0
         self.equipmentList = []
         self.jewelList = []
         self.skillPotion = 0
         self.staminaPotion = 0
         self.luckPotion = 0
         self.provision = 0

    #DEFINES PLAYER STARTING SKILL
    def skillRoll (value):
        skill = D6(1)
        print("\nTesting your SKILL...")
        print (f"You rolled: {skill}! (+6)")
        return skill + 6
    
    #DEFINES PLAYER STARTING STAMINA
    def staminaRoll (value):
        stamina = D6(2)
        print("\nTesting your STAMINA...")
        print (f"You rolled: {stamina}! (+12)")
        return stamina + 12

    #DEFINES PLAYER STARTING LUCK
    def luckRoll(value):
        luck = D6(1)
        print("\nTesting your LUCK...")
        print (f"You rolled: {luck}! (+6)")
        return luck + 6
    
    def generateCharacter(name):
        skill = Character.skillRoll(0)
        stamina = Character.staminaRoll(0)
        luck = Character.luckRoll(0)
        initial_skill = skill
        initial_stamina = stamina
        initial_luck = luck
        return skill, stamina, luck, initial_skill, initial_stamina, initial_luck

    #INFLICTS DAMAGE ON PLAYER
    def wound(self,damage):
        self.stamina = self.stamina - damage

    #HEALS PLAYER
    def heal(self, stamina):
        self.stamina = self.stamina + stamina

    #DECREASE PLAYER SKILL
    def skillDecrease(self, loss):
        self.skill = self.skill - loss
    
    #INCREASE PLAYER SKILL
    def skillIncrease(self, gain):
        self.skill = self.skill + gain

    #DECREASE PLAYER LUCK
    def luckDecrease(self, loss):
        self.luck = self.luck - loss
    
    #INCREASE PLAYER LUCK
    def luckIncrease(self, gain):
        self.luck = self.luck + gain

    #RESTORES PLAYER SKILL BACK TO INITIAL SKILL
    def useSkillPotion(self,skill,loss):
        self.skillPotion = self.skillPotion - loss
        for skill in range(self.initial_skill):
            if self.skill < self.initial_skill:
                skill = self.skillIncrease(1)
            elif self.skill == self.initial_skill:
                return skill
    
    #RESTORES PLAYER STAMINA BACK TO INITIAL STAMINA
    def useStaminaPotion(self,stamina, loss):
        self.staminaPotion = self.staminaPotion - loss
        for stamina in range(self.initial_stamina):
            if self.stamina < self.initial_stamina:
                stamina = self.heal(1)
            elif self.stamina == self.initial_stamina:
                return stamina
    
    #INCREASES INITIAL LUCK BY 1 AND THEN RESTORES ALL LUCK
    def useLuckPotion(self,luck,loss):
        self.luckPotion = self.luckPotion - loss
        self.initial_luck = self.initial_luck + 1
        for luck in range(self.initial_luck):
            if self.luck < self.initial_luck:
                luck = self.luckIncrease(1)
            elif self.luck == self.initial_luck:
                return luck
    
    #FOR TESTING LUCK
    def luckTest(self):
         self - 1
         luckRoll = D6(2)
         return luckRoll
    
    #ADD GOLD
    def addGold (self, gain):
        self.gold = self.gold + gain
    #REMOVE GOLD
    def removeGold (self, loss):
        self.gold = self.gold - loss

    #ADD PROVISION TO TOTAL PROVISIONS (MAX 10)
    def addProvision (self, gain):
        if self.provision == 10:
            print("Your backpack is full!")
        else:
            self.provision = self.provision + gain

    #USE PROVISION AND RESTORE STAMINA
    def useProvision (self, loss, staminaGain):
        print("You used a provision!")
        self.provision = self.provision - loss
        self.stamina = self.stamina + staminaGain

    def addEquipment (self, item):
        return self.equipmentList.append(item)









