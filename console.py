import sys

class Console:
    def mainMenu(x):
        active = 0
        while active == 0:
            print(f"\nFOREST OF DOOM!")
            print(f"\n1: INTRODUCTION")
            print(f"2: BEGIN ADVENTURE ")
            print(f"3: QUIT")

            choice = input("\nWhat is your choice? ")
            choice = int(choice)

            if choice == 1:
                print("\n'Ambush!' Look out! Ambush! Aagh! The hammer!")
                print("Take the hammer to Gillibran! Save the Dwarfs!")
                print("\nHis eyes half close and the pain seems to ease a little,")
                print("and as the delirium subsides, he speaks to you again")
                print("in a low whisper.")
                print("\n'Help us, friend . . . take the hammer to Gillibran")
                print(". . . Only the hammer will unite our people against")
                print("the trolls . . . We were on our way to Darkwood in")
                print("search of the hammer . . . ambushed by the little")
                print("people . . . others killed . . . the map in my pouch")
                print("will take you to the home of Yaztromo, the master")
                print("mage of these parts . . . he has great magics for sale")
                print("to protect you against the creatures of Darkwood")
                print(". . . take my gold . . .I beg you to find the hammer")
                print("and take it to Gillibran, my Lord of Stonebridge . . .")
                print("you will be well rewarded . . .")
                print("\nBigleg opens his mouth to start another sentence,")
                print("but nothing comes out except his last dying breath.")
                print("You sit down and ponder Bigleg's words. Who is")
                print("Gillibran? Who is Yaztromo? What is all the fuss")
                print("about the dwarfish hammer? You reach over to the")
                print("still body of Bigleg and remove the pouch from the")
                print("leather belt around his waist. Inside you find 30")
                print("Gold Pieces and a map.")
                print("\nJingling the coins in your hand you think of the")
                print("possible rewards which may await you just for")
                print("returning a hammer to a village of dwarfs. You")
                print("decide to try to find the hammer in Darkwood")
                print("Forest; it's been a few weeks since your last good")
                print("battle, and, what is more, you are likely to be well")
                print("paid for this one.")
                print("\nWith your mind made up, you settle down to sleep,")
                print("having taken back the sheepskin blanket from poor")
                print("Bigleg. In the morning you bury the old dwarf and")
                print("gather up your possessions. You examine the")
                print("map. look up to the sun, and find your bearings.")
                print("Whistling merrily, you head off south at a good")
                print("pace, eager to meet this man Yaztromo and see")
                print("what he has to offer...")
            elif choice == 2:
                active += 1
            elif choice ==3:
                sys.exit()
            else:
                print("invalid choice. Try again")
    def pause(x):
        pause = True
        while pause == True:
            choice = input("\nx to continue ")
            if choice == 'x':
                pause = False
            else:
                continue
    """
    def pauseBattle(x):
        pause = True
        while pause == True:
            choice = input("\nMake your choice: (1, 2, 3) ")
            choice = int(choice)
            if choice == 1:
                print("You attacked!")
            elif choice == 2:
                print("Here are your items!")
            elif choice == 3:
                print("You fled... (-2 STAMINA)")
            else:
                print("Try that again...")
    """